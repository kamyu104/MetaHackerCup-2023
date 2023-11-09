# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem D. Double Stars
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/D
#
# Time:  O(N * sqrt(N))
# Space: O(N)
#

from collections import Counter

def double_stars():
    def bfs():
        degree = [0]*N
        for _, v in enumerate(P, 1):
            degree[v] += 1
        dp_down = [0]*N
        q = [u for u in range(N) if degree[u] == 0]
        while q:
            new_q = []
            for u in q:
                if u == 0:
                    continue
                v = P[u-1]
                dp_down[v] = max(dp_down[v], dp_down[u]+1)
                degree[v] -= 1
                if degree[v] == 0:
                    new_q.append(v)
            q = new_q
        return dp_down

    def bfs2():
        adj = [[] for _ in range(N)]
        for u, v in enumerate(P, 1):
            adj[v].append(u)
        dp_up = [0]*N
        q = [0]
        while q:
            new_q = []
            for u in q:
                prefix = [-1]*(len(adj[u])+1)
                for i in range(len(adj[u])):
                    prefix[i+1] = max(prefix[i], dp_down[adj[u][i]])
                suffix = [-1]*(len(adj[u])+1)
                for i in reversed(range(len(adj[u]))):
                    suffix[i] = max(suffix[i+1], dp_down[adj[u][i]])
                for i, v in enumerate(adj[u]):
                    dp_up[v] = max(dp_up[u], prefix[i]+1, suffix[i+1]+1)+1
                    new_q.append(v)
            q = new_q
        return dp_up

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    dp_down = bfs()
    dp_up = bfs2()
    cnts = [Counter() for _ in range(N)]
    for u, v in enumerate(P, 1):
        cnts[u][dp_up[u]] += 1
        cnts[v][dp_down[u]+1] += 1
    degree = [sum(cnts[u].values()) for u in range(N)]
    sorted_cnts = [sorted(cnts[u].keys()) for u in range(N)]
    result = 0
    for u, v in enumerate(P, 1):
        cnts[u][dp_up[u]] -= 1
        cnts[v][dp_down[u]+1] -= 1
        degree1, degree2 = degree[u]-1, degree[v]-1
        prev = i = j = 0
        while i < len(sorted_cnts[u]) or j < len(sorted_cnts[v]):
            if j == len(sorted_cnts[v]) or (i < len(sorted_cnts[u]) and sorted_cnts[u][i] < sorted_cnts[v][j]):
                d = sorted_cnts[u][i]
                result += (d-prev)*min(degree1, degree2)
                prev = d
                degree1 -= cnts[u][d]
                i += 1
            else:
                d = sorted_cnts[v][j]
                result += (d-prev)*min(degree1, degree2)
                prev = d
                degree2 -= cnts[v][d]
                j += 1
        cnts[v][dp_down[u]+1] += 1
        cnts[u][dp_up[u]] += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, double_stars()))
