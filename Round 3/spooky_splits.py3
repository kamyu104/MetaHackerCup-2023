# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem A. Spooky Splits
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/A
#
# Time:  O(D * S * N) = O(S * NlogN), D = len(divisors(N)) = O(logN) on average, S = sum(len(partitions(i)) for i in range(1, N+1)) = 1,642,992,567 at most if N = 100 which is much larger than it really is
# Space: O(S * N)
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
            if total == N:
                return True
            fs = frozenset(curr.items())
            if fs in lookup:
                return False
            lookup.add(fs)
            for j in range(i, len(sorted_cnt_keys)):
                k = sorted_cnt_keys[j]
                if not (total%target+k <= target):
                    break
                if not ((curr[k] if k in curr else 0)+1 <= cnts[k]):
                    continue
                curr[k] += 1
                if backtracking(j if (total+k)%target else 0, total+k, curr):
                    return True
                curr[k] -= 1
                if not curr[k]:
                    del curr[k]
            return False

        if N%K:
            return False
        target = N//K
        if sorted_cnt_keys[-1] > target:
            return False
        lookup = set()
        return backtracking(0, 0, Counter())

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
