# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem D. Today is Gonna be a Great Day
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/D
#
# Time:  O(QlogN)
# Space: O(N)
#

# Template:
# https://github.com/kamyu104/GoogleCodeJam-2022/blob/main/Round%203/duck_duck_geese.py3
class SegmentTree(object):  # 0-based index
    def __init__(self, N,
                 build_fn=lambda _: 0,
                 query_fn=lambda x, y: y if x is None else max(x, y),
                 update_fn=lambda x, y: y if x is None else x+y,
                 update_lazy_fn=lambda x, y: y if x is None else x+y):  # added
        self.base = N
        self.H = (N-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.update_lazy_fn = update_lazy_fn  # added
        self.tree = [None]*(2*N)
        self.lazy = [None]*N
        for i in range(self.base, self.base+N):
            self.tree[i] = build_fn(i-self.base)
        for i in reversed(range(1, self.base)):
            self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.base:
            self.lazy[x] = self.update_lazy_fn(self.lazy[x], val)  # modified

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

    def query(self, L, R):  # Time: O(logN), Space: O(N)
        def push(x):
            n = self.H
            while n:
                y = x >> n
                if self.lazy[y] is not None:
                    self.__apply(y<<1, self.lazy[y])
                    self.__apply((y<<1)+1, self.lazy[y])
                    self.lazy[y] = None
                n -= 1

        result = None
        if L > R:
            return result

        L += self.base
        R += self.base
        push(L)
        push(R)
        while L <= R:
            if L & 1:  # is right child
                result = self.query_fn(result, self.tree[L])
                L += 1
            if R & 1 == 0:  # is left child
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L >>= 1
            R >>= 1
        return result

def today_is_gonna_be_a_great_day():
    def build(i):
        return [A[i], -i]

    def update(x, y):
        return [(x[0]*y)%MOD, x[1]]

    def update_lazy(x, y):
        return y if x is None else (x*y)%MOD

    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L_R = list(map(lambda x: int(x)-1, input().split()) for _ in range(Q))
    st = SegmentTree(N, build_fn=build, update_fn=update, update_lazy_fn=update_lazy)
    st.update(0, N-1, MOD-1)
    result = 0
    for L, R in L_R:
        st.update(L, R, MOD-1)
        result += -st.query(L, R)[1]+1
    return result

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, today_is_gonna_be_a_great_day()))
