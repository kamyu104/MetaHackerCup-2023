# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem D. Today is Gonna be a Great Day
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/D
#
# Time:  O(NlogN + QlogN)
# Space: O(N)
#

# Template:
# https://github.com/kamyu104/GoogleCodeJam-2022/blob/main/Round%203/duck_duck_geese.py3
class SegmentTree(object):  # 0-based index
    def __init__(self, N,
                 build_fn=lambda _: 0,
                 query_fn=lambda x, y: y if x is None else max(x, y),
                 update_fn=lambda x, y: y if x is None else x+y):
        self.base = N
        self.H = (N-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.tree = [None]*(2*N)
        self.lazy = [None]*N
        for i in range(self.base, self.base+N):
            self.tree[i] = build_fn(i-self.base)
        for i in reversed(range(1, self.base)):
            self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.base:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def __push(self, x):
        n = self.H
        while n:
            y = x >> n
            if self.lazy[y] is not None:
                self.__apply(y<<1, self.lazy[y])
                self.__apply((y<<1)+1, self.lazy[y])
                self.lazy[y] = None
            n -= 1

    def update(self, L, R, h):  # Time: O(logN), Space: O(N)
        def pull(x):
            while x > 1:
                x >>= 1
                self.tree[x] = self.query_fn(self.tree[x<<1], self.tree[(x<<1)+1])
                if self.lazy[x] is not None:
                    self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

        if L > R:
            return
        L += self.base
        R += self.base
        L0, R0 = L, R
        while L <= R:
            if L & 1:  # is right child
                self.__apply(L, h)
                L += 1
            if R & 1 == 0:  # is left child
                self.__apply(R, h)
                R -= 1
            L >>= 1
            R >>= 1
        pull(L0)
        pull(R0)

def today_is_gonna_be_a_great_day():
    def build(i):
        return [(A[i], -i), ((-A[i])%MOD, -i)]

    def query(x, y):
        return y if x is None else [max(x[0], y[0]), max(x[1], y[1])]

    def update(x, y):
        if x is None:
            return y
        if len(x) == 1:
            return [x[0]^y[0]]
        if y[0]:
            x[0], x[1] = x[1], x[0]
        return x

    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L_R = [list(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]
    st = SegmentTree(N, build_fn=build, query_fn=query, update_fn=update)
    result = 0
    for L, R in L_R:
        st.update(L, R, [1])
        result += -st.tree[1][0][1]+1
    return result

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, today_is_gonna_be_a_great_day()))
