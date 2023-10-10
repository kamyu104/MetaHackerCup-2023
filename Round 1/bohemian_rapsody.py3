# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem E. Bohemian Rap-sody
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/E
#
# Time:  O(QlogN + QlogQ + (L + Q) * sqrt(N)), L = sum(min(len(w), MAX_K) for w in W), pass in PyPy3 but Python3
# Space: O(Q + N)
#

from bisect import bisect_left, bisect_right

def bohemian_rapsody():
    def new_node():
        curr.append([None]*26)
        return len(curr)-1

    # reference: https://cp-algorithms.com/data_structures/sqrt_decomposition.html
    def mo_s_algorithm(a, queries):  # Time: O(QlogQ + (N + Q) * sqrt(N))
        def add(i):  # Time: O(F) = O(1)
            idx = lookup[a[i]]
            suffix[cnt[idx]] += 1
            cnt[idx] += 1

        def remove(i):  # Time: O(F) = O(1)
            idx = lookup[a[i]]
            cnt[idx] -= 1
            suffix[cnt[idx]] -= 1

        def get_ans(l):  # Time: O(A) = O(sqrt(N))
            ans = suffix[0]
            for i in range(1, len(suffix)):
                if i >= ans:
                    break
                assert((i+1)*i//2 <= l)
                ans = min(ans, i+suffix[(i-1)+1])
            return ans

        block_size = int(len(a)**0.5)  # O(S) = O(sqrt(N))
        queries.sort(key=lambda x: (x[0]//block_size, x[1]))  # Time: O(QlogQ)
        left, right = 0, -1
        for l, r in queries:  # Time: O((N / S) * N * F + S * Q * F + Q * A) = O((N + Q) * sqrt(N)), O(S) = O(sqrt(N)), O(F) = O(1), O(A) = O(sqrt(N))
            while left > l:
                left -= 1
                add(left)
            while right < r:
                right += 1
                add(right)
            while left < l:
                remove(left)
                left += 1
            while right > r:
                remove(right)
                right -= 1
            yield get_ans(right-left+1)

    N = int(input())
    W = [list(map(lambda x: ord(x)-ord('a'), input()))[::-1] for _ in range(N)]
    Q = int(input())
    A_B_K = [list(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]
    max_l = max(len(w) for w in W)
    max_k = max(K for _, _, K in A_B_K)+1
    groups = [[] for _ in range(min(max_l, max_k))]
    for A, B, K in A_B_K:
        if K < len(groups):
            groups[K].append((A, B))
    curr = []
    new_node()
    alives = list(range(N))
    lookup, suffix = [0]*N, [0]*N
    result = 0
    for k, group in enumerate(groups):
        alives = [i for i in alives if k < len(W[i])]
        prev, curr = curr, []
        for i in alives:
            if prev[lookup[i]][W[i][k]] is None:
                prev[lookup[i]][W[i][k]] = new_node()
            lookup[i] = prev[lookup[i]][W[i][k]]
        if not group:
            continue
        cnt = [0]*len(curr)
        for i in range(len(alives)):
            suffix[i] = 0
        qs = [(bisect_left(alives, l), bisect_right(alives, r)-1) for l, r in group]  # Time: O(QlogN)
        result += sum(ans for ans in mo_s_algorithm(alives, qs))
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, bohemian_rapsody()))
