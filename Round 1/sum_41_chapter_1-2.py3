# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem B1. Sum 41 (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1
#
# Time:  O(backtracking_nodes(K)) = O(89166), K = 41
# Space: O(K)
#

def sum_41_chapter_1():
    def backtracking(total, product):
        if total == 0:
            return product == 1
        for i in range(result[-1] if result else 1, total+1):
            if i > total-i != 0 or product%i:
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
