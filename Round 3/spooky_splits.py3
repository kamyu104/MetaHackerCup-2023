# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem A. Spooky Splits
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/a
#
# Time:  O(?)
# Space: O(?)
#

from collections import Counter

def spooky_splits():
    def bfs(u):
        result = 0
        lookup[u] = True
        q = [u]
        while q:
            new_q = []
            result += len(q)
            for u in q:
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    lookup[v] = True
                    new_q.append(v)
            q = new_q
        return result

    def check(K, N):
        def backtracking(i, total, curr):
            if total == target:
                sorted_partitions.append(list(curr.items()))
                return
            for j in range(i, len(sorted_cnt_keys)):
                k = sorted_cnt_keys[j]
                if not (total+k <= target):
                    break
                curr[k] += 1
                if curr[k] <= cnts[k]:
                    backtracking(j, total+k, curr)
                curr[k] -= 1
                if not curr[k]:
                    del curr[k]

        def backtracking2(i, total, curr):
            if total == K:
                return True
            for j in range(i, len(sorted_partitions)):
                for k, v in sorted_partitions[j]:
                    curr[k] += v
                if all(curr[k] <= cnts[k] for k in curr.keys()) and backtracking2(j, total+1, curr):
                    return True
                for k, v in sorted_partitions[j]:
                    curr[k] -= v
                    if not curr[k]:
                        del curr[k]
            return False

        if N%K:
            return False
        target = N//K
        sorted_partitions = []
        backtracking(0, 0, Counter())
        return backtracking2(0, 0, Counter())

    N, M = list(map(int, input().split()))
    A_B = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    adj = [[] for _ in range(N)]
    for u, v in A_B:
        adj[u].append(v)
        adj[v].append(u)
    lookup = [False]*N
    cnts = Counter(bfs(u) for u in range(N) if not lookup[u])
    sorted_cnt_keys = [k for k in range(1, N+1) if k in cnts]
    result = [K for K in range(1, N+1) if check(K, N)]
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, spooky_splits()))
