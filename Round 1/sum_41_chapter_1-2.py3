# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem B1. Sum 41 (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1
#
# Time:  O(backtracking_nodes(K) + K^2) = O(partitions(K)*2 + K^2) = O(89166 + K^2), K = 41
# Space: O(K)
#

from itertools import chain

def sum_41_chapter_1():
    def backtracking(total, product):
        if total == 0:
            return product == 1
        for i in chain(range(result[-1] if result else 1, total//2+1), [total]):
            if product%i:
                continue
            result.append(i)
            if backtracking(total-i, product//i):
                return True
            result.pop()
        return False

    P = int(input())
    result = []
    return f'{len(result)} {" ".join(map(str, result))}' if backtracking(TARGET, P) else -1

TARGET = 41
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sum_41_chapter_1()))
