# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem F. Cacti Cartography
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/F
#
# Time:  O(N^3)
# Space: O(N^2)
#

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

    def iter_dfs():  # Time: O(M)
        parent, in_cycle, cycles = [-2]*N, [False]*N, [[] for _ in range(N)]
        idxs = [-1]*N
        idx = 0
        stk = [(0, -1)]
        while stk:
            u, p = stk.pop()
            if idxs[u] != -1:
                if idxs[u] < idxs[p]:
                    cycle = []
                    while p != u:
                        in_cycle[p] = True
                        cycle.append(p)
                        p = parent[p]
                    cycles[u].append(cycle)
                continue
            idxs[u] = idx
            idx += 1
            parent[u] = p
            for v in adj[u]:
                if v == parent[u]:
                    continue
                stk.append((v, u))
        return idxs, parent, in_cycle, cycles

    N, M, K = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A_B = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    adj = [[] for _ in range(N)]
    for u, v in A_B:
        adj[u].append(v)
        adj[v].append(u)
    dist = [bfs(u) for u in range(N)]
    idxs, parent, in_cycle, cycles = iter_dfs()
    order = [-1]*N
    for i, x in enumerate(idxs):
        order[x] = i
    dp = [[0 if dist[u][v] <= K else INF for v in range(N)] for u in range(N)]
    for u in reversed(order):
        for v in adj[u]:  # Total Time: O(N * M)
            if parent[v] != u or in_cycle[v]:
                continue
            mn = min(dp[v][w]+C[w] for w in range(N))
            for w in range(N):
                dp[u][w] += min(dp[v][w], mn)
        for cycle in cycles[u]:  # Total Time: O(N^3)
            dp2 = [[INF]*(len(cycle)+1) for _ in range(len(cycle))]
            for v in range(N):
                for i in range(len(dp2)):
                    prefix = C[v]
                    for j in range(i+1, len(dp2[i])):
                        prefix += dp[cycle[j-1]][v]
                        dp2[i][j] = min(dp2[i][j], prefix)
            for v in range(N):
                prefix = dp[u][v]
                dp3 = [INF]*(len(cycle)+1)
                for i in range(len(dp3)):
                    if i-1 >= 0:
                        prefix += dp[cycle[i-1]][v]
                        dp[u][v] += dp[cycle[i-1]][v]
                    dp3[i] = min(dp3[i], prefix)
                    dp[u][v] = min(dp[u][v], dp3[i])
                    for j in range(i+1, len(dp3)):
                        dp3[j] = min(dp3[j], dp3[i]+dp2[i][j])
    return min(dp[0][u]+C[u] for u in range(N))

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cacti_cartography()))