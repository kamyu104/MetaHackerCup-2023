# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem E. Dealing Decks
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/E
#
# Time:  O(NlogN), pass in PyPy3 but Python3
# Space: O(NlogN)
#

class PersistentTrie(object):
    def __init__(self, N):
        self.__bit_length = N.bit_length()
        self.__versions = [0]*(N+1)
        self.__new_nodes = [0]*(self.__bit_length+1)
        self.__length = 1
        self.__nodes = [[0]*2 for _ in range(len(self.__versions)*len(self.__new_nodes)+1)]
        self.__mins = [-1]*(len(self.__versions)*len(self.__new_nodes)+1)

    def __copy_node(self, x):
        self.__nodes[self.__length][0] = self.__nodes[x][0]
        self.__nodes[self.__length][1] = self.__nodes[x][1]
        self.__mins[self.__length] = self.__mins[x]
        self.__length += 1
        return self.__length-1

    def add(self, i, x):
        self.__new_nodes[-1] = self.__copy_node(self.__versions[i-1] if i-1 >= 0 else 0)
        for d in reversed(range(1, self.__bit_length+1)):
            self.__new_nodes[d-1] = self.__copy_node(self.__nodes[self.__new_nodes[d]][(x>>(d-1))&1])
        self.__mins[self.__new_nodes[0]] = i
        for d in range(1, self.__bit_length+1):
            self.__nodes[self.__new_nodes[d]][(x>>(d-1))&1] = self.__new_nodes[d-1]
            self.__mins[self.__new_nodes[d]] = min(self.__mins[self.__nodes[self.__new_nodes[d]][0]], self.__mins[self.__nodes[self.__new_nodes[d]][1]])
        self.__versions[i] = self.__new_nodes[-1]

    def query(self, l, r, x):
        result = 0
        curr = self.__versions[r]
        for d in reversed(range(1, self.__bit_length+1)):
            u = (x>>(d-1))&1
            if self.__mins[self.__nodes[curr][u]] < l:
                curr = self.__nodes[curr][u]
            else:
                curr = self.__nodes[curr][u^1]
                result |= 1<<(d-1)
        return result

    def reset(self):
        self.__length = 1

def dealing_decks():
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
    PT.reset()
    PT.add(0, 0)
    lookup = [-1]*(N+1)
    grundy = [0]*(N+1)
    result = 0
    for i in range(1, N+1):
        grundy[i] = PT.query(i-B[i], i-A[i], grundy[C[i]])
        assert(0 <= grundy[i] <= N)
        if lookup[grundy[i]] == -1:
            lookup[grundy[i]] = i
        result += lookup[grundy[i]]
        PT.add(i, grundy[i])
    return result

MAX_N = 2000000
PT = PersistentTrie(MAX_N)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, dealing_decks()))
