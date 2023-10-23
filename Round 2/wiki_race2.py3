# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 2 - Problem C. Wiki Race
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/C
#
# Time:  O(N + M * logL * MAX_S), M = sum(M[i] for i in range(N)), L = number of leaves, MAX_S = O(10)
# Space: O(N + M * MAX_S)
#

from collections import Counter

def wiki_race():
    def iter_dfs():
        stk = [0]
        while stk:
            u = stk.pop()
            while len(adj[u]) == 1:
                v = adj[u][0]
                for x in S[v]:
                    S[u].add(x)
                adj[u] = adj[v]
            for v in adj[u]:
                stk.append(v)

    def iter_dfs2():
        lookup = set()
        ret = Counter()
        stk = [(1, (0, ret))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                u, ret = args
                rets = [Counter() for _ in range(len(adj[u]))]
                stk.append((2, (u, rets, ret)))
                for i, v in enumerate(adj[u]):
                    stk.append((1, (v, rets[i])))
            elif step == 2:
                u, rets, ret = args
                cnt = Counter(S[u])
                if not rets:
                    for k, v in cnt.items():
                        if k in lookup:
                            continue
                        ret[k] = v
                    continue
                for c in rets:
                    for k, v in c.items():
                        cnt[k] += v
                for k, v in cnt.items():
                    if k in lookup:
                        continue
                    if v >= len(adj[u]):
                        ret[k] = 1
                    elif v+int(k not in S[u]) == len(adj[u]):
                        ret[k] = 0
                    else:
                        lookup.add(k)
        return sum(ret.values())

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    S = [set(input().split()[1:]) for _ in range(N)]
    lookup = {}
    for i in range(N):
        for x in S[i]:
            if x not in lookup:
                lookup[x] = len(lookup)
        S[i] = {lookup[x] for x in S[i]}
    adj = [[] for _ in range(N)]
    for i, p in enumerate(P, 1):
        adj[p].append(i)
    iter_dfs()
    return iter_dfs2()

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, wiki_race()))