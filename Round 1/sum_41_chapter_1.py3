# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem B1. Sum 41 (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1
#
# Time:  O(sqrt(P))
# Space: O(sqrt(P))
#

def sum_41_chapter_1():
    TARGET = 41
    P = int(input())
    result = []
    p = 2
    while p*p <= P:
        while P%p == 0:
            P //= p
            result.append(p)
        p += 1
    if P != 1:
        result.append(P)
    if sum(result) > TARGET:
        return -1
    result.extend((1 for _ in range(TARGET-sum(result))))
    return f'{len(result)} {" ".join(map(str, result))}'

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sum_41_chapter_1()))
