# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 2 - Problem C. Wiki Race
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/C
#
# Time:  O(M * MAX_S), M = sum(M[i] for i in range(N)), MAX_S = O(10)
# Space: O(M * MAX_S)
#

def wiki_race():
    def iter_dfs():
        cnt = [0]*len(lookup)
        leaves = 0
        stk = [0]
        while stk:
            u = stk.pop()
            while len(adj[u]) == 1:
                v = adj[u][0]
                for x in S[v]:
                    S[u].add(x)
                adj[u] = adj[v]
            for x in S[u]:
                cnt[x] += 1
            if not adj[u]:
                leaves += 1
                continue
            for v in adj[u]:
                stk.append(v)
        return cnt, leaves

    def iter_dfs2(x):
        ret = [0]
        stk = [(1, (0, ret))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                u, ret = args
                rets = [[0] for _ in range(len(adj[u]))]
                stk.append((2, (u, rets, ret)))
                for i, v in enumerate(adj[u]):
                    stk.append((1, (v, rets[i])))
            elif step == 2:
                u, rets, ret = args
                if not rets:
                    ret[0] = int(x in S[u])
                    continue
                cnt = sum(r[0] for r in rets)
                if cnt == len(adj[u]):
                    ret[0] = 1
                    continue
                if cnt == len(adj[u])-1:
                    ret[0] = int(x in S[u])
                    continue
                return 0
        return int(ret[0] == 1)

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    S = [input().split()[1:] for _ in range(N)]
    lookup = {}
    for i in range(N):
        for x in S[i]:
            if x not in lookup:
                lookup[x] = len(lookup)
        S[i] = {lookup[x] for x in S[i]}
    adj = [[] for _ in range(N)]
    for i, p in enumerate(P, 1):
        adj[p].append(i)
    cnt, leaves = iter_dfs()
    return sum(iter_dfs2(k) for k, v in enumerate(cnt) if v >= leaves)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, wiki_race()))
