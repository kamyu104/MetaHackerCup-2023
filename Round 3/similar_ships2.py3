# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem E. Similar Ships
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/E
#
# Time:  O(N)
# Space: O(N)
#

def similar_ships():
    def iter_dfs():
        result = 0
        lookup = [-1]*N
        stk = [(1, 0)]
        while stk:
            step, u = stk.pop()
            if step == 1:
                stk.append((2, u))
                for v in reversed(adj[u]):
                    stk.append((1, v))
            elif step == 2:
                mx1 = mx2 = 0
                for v in adj[u]:
                    tmp = lookup[v]
                    if tmp > mx1:
                        mx1, tmp = tmp, mx1
                    if tmp > mx2:
                        mx2, tmp = tmp, mx2
                result = max(result, mx1+mx2)
                lookup[u] = mx1+1
        return result

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    adj = [[] for _ in range(N)]
    for u, v in enumerate(P, 1):
        adj[v].append(u)
    d = iter_dfs()
    return (N+(N-d))*(d+1)//2 % MOD

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, similar_ships()))
