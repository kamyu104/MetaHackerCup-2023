# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem B2. Sum 41 (Chapter 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B2
#
# Time:  O(backtracking_nodes(K) + K^2) = O(259891 + K^2), K = 41
# Space: O(K)
#

def sum_41_chapter_2():
    def backtracking(total, product, curr):
        if total == 0:
            if product == 1:
                if not result or len(result) > len(curr):
                    result[:] = curr
            return
        for i in reversed(range(1, min(total, curr[-1] if curr else INF)+1)):
            if product%i:
                continue
            curr.append(i)
            backtracking(total-i, product//i, curr)
            curr.pop()

    P = int(input())
    result = []
    backtracking(TARGET, P, [])
    return f'{len(result)} {" ".join(map(str, result))}' if result else -1

INF = float("inf")
TARGET = 41
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sum_41_chapter_2()))
