# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem E. Similar Ships
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/E
#
# Time:  O(N)
# Space: O(N)
#

def similar_ships():
    def bfs(u):
        result = [0, None]
        lookup = [False]*N
        lookup[u] = True
        q = [u]
        while q:
            result = [result[0]+1, q[0]]
            new_q = []
            for u in q:
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    lookup[v] = True
                    new_q.append(v)
            q = new_q
        return result

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    adj = [[] for _ in range(N)]
    for u, v in enumerate(P, 1):
        adj[u].append(v)
        adj[v].append(u)
    _, u = bfs(0)
    d, _ = bfs(u)
    return ((N-1+1)+(N-d+1))*d//2 % MOD

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, similar_ships()))
