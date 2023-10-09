# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem E. Bohemian Rap-sody
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/E
#
# Time:  O(QlogN + QlogQ + (L + Q) * sqrt(N)), L = sum(len(w) for w in W), pass in PyPy3 but Python3
# Space: O(Q + T), T is the size of trie
#

from bisect import bisect_left, bisect_right

def bohemian_rapsody(): 
    def new_node():
        trie.append([0]*26)
        return len(trie)-1

    # reference: https://cp-algorithms.com/data_structures/sqrt_decomposition.html
    def mo_s_algorithm():  # Time: O(QlogQ + (N + Q) * sqrt(N))
        def add(i, x):
            idx = lookup[idxs[i]]
            cnt2[cnt[idx]] -= 1
            cnt[idx] += x
            cnt2[cnt[idx]] += 1

        def get_ans():  # Time: sqrt(N)
            ans = remain = -cnt2[0]
            for i in range(1, len(cnt2)):
                if i >= ans:
                    break
                remain -= cnt2[i]
                ans = min(ans, i+remain)
            return ans

        block_size = int(len(idxs)**0.5)
        queries.sort(key=lambda x: (x[0]//block_size, x[1]))  # Time: O(QlogQ)
        left, right = 0, -1
        for l, r in queries:  # Time: O((N + Q) * sqrt(N))
            while left > l:
                left -= 1
                add(left, +1)
            while right < r:
                right += 1
                add(right, +1)
            while left < l:
                add(left, -1)
                left += 1
            while right > r:
                add(right, -1)
                right -= 1
            yield get_ans()
        for i in range(left, right+1):
            add(i, -1)

    N = int(input())
    W = [list(map(lambda x: ord(x)-ord('a'), input()))[::-1] for _ in range(N)]
    Q = int(input())
    A_B_K = [map(lambda x: int(x)-1, input().split()) for _ in range(Q)]

    max_l = max(len(w) for w in W)
    qs = [[] for _ in range(max_l)]
    for A, B, K in A_B_K:
        if K < len(qs):
            qs[K].append((A, B))

    trie = [[0]*26]
    for w in W:
        idx = 0
        for c in w:
            if not trie[idx][c]:
                trie[idx][c] = new_node()
            idx = trie[idx][c]

    cnt = [0]*len(trie)
    cnt2 = [0]*(N+1)
    lookup = [0]*N
    idxs = list(range(N))
    result = 0
    for k, queries in enumerate(qs):
        new_idxs = []
        for i in idxs:
            if not k < len(W[i]):
                continue
            lookup[i] = trie[lookup[i]][W[i][k]]
            if lookup[i]:
                new_idxs.append(i)
        idxs = new_idxs
        queries = [(bisect_left(idxs, l), bisect_right(idxs, r)-1) for l, r in queries]
        result += sum(ans for ans in mo_s_algorithm())
    return result
    
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, bohemian_rapsody()))
