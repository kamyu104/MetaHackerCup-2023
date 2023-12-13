# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem C. Resisting Robots
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/C
#
# Time:  O(NlogN + M)
# Space: O(N + M)
#

def resisting_robots():
    class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
        def __init__(self, arr):  # modified
            self.set = list(range(len(arr)))
            self.ranks = [0]*len(arr)
            self.last = list(range(len(arr)))  # added
            self.total = arr[:]  # added
            self.p = [-1]*len(arr)  # added

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
            if self.ranks[x] > self.ranks[y]:  # union by ranks
                x, y = y, x
            self.set[x] = self.set[y]
            if self.ranks[x] == self.ranks[y]:
                self.ranks[y] += 1
            self.last[y] = prev_x  # added
            self.total[prev_x] += self.total[prev_y]  # added
            self.p[prev_y] = prev_x  # added
            return True

    N, M = list(map(int, input().split()))
    P = list(map(int, input().split()))
    roads = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    idxs = list(range(N))
    idxs.sort(key=lambda x: P[x])
    ranks = [0]*N
    for i, x in enumerate(idxs):
        ranks[x] = i
    adj = [[] for _ in range(N)]
    for u, v in roads:
        if ranks[u] < ranks[v]:
            u, v = v, u
        adj[u].append(v)
    uf = UnionFind(P)
    for u in idxs:
        for v in adj[u]:
            uf.union_set(u, v)
    result = [0]*N
    for i in reversed(range(N-1)):
        result[idxs[i]] = max(result[uf.p[idxs[i]]], P[uf.p[idxs[i]]]-uf.total[idxs[i]])
    return sum(result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, resisting_robots()))
