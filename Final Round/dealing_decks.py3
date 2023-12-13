# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem E. Dealing Decks
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/E
#
# Time:  O(NlogN), pass in PyPy3 but Python3
# Space: O(NlogN)
#

def dealing_decks():
    class PersistentTrie(object):
        def __init__(self, N):
            self.__length = 0
            NODES[self.__length][0] = 0
            NODES[self.__length][1] = 0
            MINS[self.__length] = -1
            self.__length += 1

        def __copy_node(self, x):
            NODES[self.__length][0] = NODES[x][0]
            NODES[self.__length][1] = NODES[x][1]
            MINS[self.__length] = MINS[x]
            self.__length += 1
            return self.__length-1

        def add(self, i, x):
            NEW_NODES[-1] = self.__copy_node(VERSIONS[i-1] if i-1 >= 0 else 0)
            for d in reversed(range(1, len(NEW_NODES))):
                NEW_NODES[d-1] = self.__copy_node(NODES[NEW_NODES[d]][(x>>(d-1))&1])
            MINS[NEW_NODES[0]] = i
            for d in range(1, len(NEW_NODES)):
                NODES[NEW_NODES[d]][(x>>(d-1))&1] = NEW_NODES[d-1]
                MINS[NEW_NODES[d]] = min(MINS[NODES[NEW_NODES[d]][0]], MINS[NODES[NEW_NODES[d]][1]])
            VERSIONS[i] = NEW_NODES[-1]
            return VERSIONS[i]

        def query(self, l, r, x):
            result = 0
            curr = VERSIONS[r]
            for d in reversed(range(1, len(NEW_NODES))):
                u = (x>>(d-1))&1
                if MINS[NODES[curr][u]] < l:
                    curr = NODES[curr][u]
                else:
                    curr = NODES[curr][u^1]
                    result |= 1<<(d-1)
            return result

    N = int(input())
    Xa, Ya, Za, Xb, Yb, Zb, Xc, Yc, Zc = list(map(int, input().split()))
    A, B, C = [0]*(N+1), [0]*(N+1), [0]*(N+1)
    Pa =  Pb = Pc = 0
    for i in range(1, N+1):
        Pa = (Pa*Xa+Ya)%Za
        Pb = (Pb*Xb+Yb)%Zb
        Pc = (Pc*Xc+Yc)%Zc
        A[i] = min(i, 1+Pa)
        B[i] = max(A[i], i-Pb)
        C[i] = min(i-1, Pc)
    pt = PersistentTrie(N)
    pt.add(0, 0)
    lookup = [-1]*(N+1)
    grundy = [0]*(N+1)
    result = 0
    for i in range(1, N+1):
        grundy[i] = pt.query(i-B[i], i-A[i], grundy[C[i]])
        assert(0 <= grundy[i] <= N)
        if lookup[grundy[i]] == -1:
            lookup[grundy[i]] = i
        result += lookup[grundy[i]]
        pt.add(i, grundy[i])
    return result

MAX_N = 2000000
MAX_BIT_LENGTH = MAX_N.bit_length()
VERSIONS = [0]*(MAX_N+1)
NEW_NODES = [0]*(MAX_BIT_LENGTH+1)
MAX_NODE_COUNT = len(VERSIONS)*len(NEW_NODES)+1
NODES = [[0]*2 for _ in range(MAX_NODE_COUNT)]
MINS = [-1]*MAX_NODE_COUNT
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, dealing_decks()))
