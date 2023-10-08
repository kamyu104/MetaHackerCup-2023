# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem B1. Sum 41 (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1
#
# Time:  O(sqrt(P))
# Space: O(K), K = 41
#

def sum_41_chapter_1():
    P = int(input())
    result = []
    total = 0
    p = 2
    while p*p <= P:
        while P%p == 0:
            P //= p
            result.append(p)
            total += result[-1]
            if total > TARGET:
                return -1
        p += 1
    if P != 1:
        result.append(P)
        total += result[-1]
        if total > TARGET:
            return -1
    result.extend((1 for _ in range(TARGET-sum(result))))
    return f'{len(result)} {" ".join(map(str, result))}'

TARGET = 41
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sum_41_chapter_1()))
