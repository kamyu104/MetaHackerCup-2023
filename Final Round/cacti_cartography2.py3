# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem F. Cacti Cartography
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/F
#
# Time:  O(N * M + T) = O(N^2 + T), T = time complexity of simplex method
# Space: O(N^2 + S), S = space complexity of simplex method
#

from pulp import *

def cacti_cartography():
    def bfs(u):  # Time: O(M)
        dist = [-1]*N
        dist[u] = d = 0
        q = [u]
        while q:
            d += 1
            new_q = []
            for u in q:
                for v in adj[u]:
                    if dist[v] != -1:
                        continue
                    dist[v] = d
                    new_q.append(v)
            q = new_q
        return dist

    N, M, K = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A_B = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    assert(M <= 3*(N-1)//2)  # cactus graph, see https://mathoverflow.net/questions/425622/the-upper-bound-of-edges-of-the-generalized-cactus-graphs
    adj = [[] for _ in range(N)]
    for u, v in A_B:
        adj[u].append(v)
        adj[v].append(u)
    dist = [bfs(u) for u in range(N)]
    x = LpVariable.dicts("x", range(N), lowBound=0, upBound=1, cat=LpBinary)
    prob = LpProblem(sense=LpMinimize)
    for u in range(N):
        prob += lpSum(x[v] for v in range(N) if dist[u][v] <= K) >= 1
    prob += lpSum(C[u]*x[u] for u in range(N))
    prob.solve(PULP_CBC_CMD(msg=False))
    return round(prob.objective.value())

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cacti_cartography()))
