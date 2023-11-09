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
    def iter_dfs():
        dp_down = [0]*N
        stk = [(1, 0)]
        while stk:
            step, u = stk.pop()
            if step == 1:
                stk.append((2, u))
                for v in adj[u]:
                    stk.append((1, v))
            elif step == 2:
                dp_down[u] = max((dp_down[v]+1 for v in adj[u]), default=0)
        return dp_down

    def iter_dfs2():
        dp_up = [0]*N
        stk = [0]
        while stk:
            u = stk.pop()
            prefix = [-1]*(len(adj[u])+1)
            for i in range(len(adj[u])):
                prefix[i+1] = max(prefix[i], dp_down[adj[u][i]])
            suffix = [-1]*(len(adj[u])+1)
            for i in reversed(range(len(adj[u]))):
                suffix[i] = max(suffix[i+1], dp_down[adj[u][i]])
            for i, v in enumerate(adj[u]):
                dp_up[v] = max(dp_up[u], prefix[i]+1, suffix[i+1]+1)+1
                stk.append(v)
        return dp_up

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    adj = [[] for _ in range(N)]
    for u, v in enumerate(P, 1):
        adj[v].append(u)
    dp_down = iter_dfs()
    dp_up = iter_dfs2()
    cnts = [Counter() for _ in range(N)]
    for u, v in enumerate(P, 1):
        cnts[u][dp_up[u]] += 1
        cnts[v][dp_down[u]+1] += 1
    sorted_cnts = [sorted(cnts[u].keys()) for u in range(N)]
    result = 0
    for u, v in enumerate(P, 1):
        cnts[u][dp_up[u]] -= 1
        cnts[v][dp_down[u]+1] -= 1
        degree1, degree2 = len(adj[u])-int(u == 0), len(adj[v])-int(v == 0)
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
