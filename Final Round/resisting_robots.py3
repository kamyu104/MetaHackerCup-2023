# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem C. Resisting Robots
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/C
#
# Time:  O(NlogN)
# Space: O(N)
#

def resisting_robots():
    class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
        def __init__(self, n, arr):  # modified
            self.set = list(range(n))
            self.rank = [0]*n
            self.last = list(range(n))  # added
            self.total = arr[:]  # added
            self.p = [-1]*N  # added

        def find_set(self, x):
            stk = []
            while self.set[x] != x:  # path compression
                stk.append(x)
                x = self.set[x]
            while stk:
                self.set[stk.pop()] = x
            return x

        def union_set(self, x, y):
            x, y = self.find_set(x), self.find_set(y)
            if x == y:
                return False
            prev_x, prev_y = self.last[x], self.last[y]  # added
            if self.rank[x] > self.rank[y]:  # union by rank
                x, y = y, x
            self.set[x] = self.set[y]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.last[y] = prev_x  # add
            self.total[prev_x] += self.total[prev_y]  # added
            self.p[prev_y] = prev_x  # added
            return True

    N, M = list(map(int, input().split()))
    P = list(map(int, input().split()))
    road = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    idxs = list(range(N))
    idxs.sort(key=lambda x: P[x])
    rank = [0]*N
    for i, x in enumerate(idxs):
        rank[x] = i
    adj = [[] for _ in range(N)]
    for u, v in road:
        if rank[u] < rank[v]:
            u, v = v, u
        adj[u].append(v)
    uf = UnionFind(N, P)
    for u in idxs:
        for v in adj[u]:
            uf.union_set(u, v)
    result = [0]*N
    for i in reversed(range(N-1)):
        result[idxs[i]] = max(result[uf.p[idxs[i]]], P[uf.p[idxs[i]]]-uf.total[idxs[i]])
    return sum(result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, resisting_robots()))
