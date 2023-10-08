# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem B1. Sum 41 (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1
#
# Time:  O(partitions(K) * K) = O(44583 * K), K = 41
# Space: O(K)
#

from functools import reduce

# reference: https://www.geeksforgeeks.org/generate-unique-partitions-of-an-integer/
def next_partition(n):
    p = [0]*n 
    k = 0
    p[k] = n
    while True:
        yield p[:k+1]
        rem_val = 0
        while k >= 0 and p[k] == 1:
            rem_val += p[k]
            k -= 1
        if k < 0:
            return
        p[k] -= 1
        rem_val += 1
        while rem_val > p[k]:
            p[k+1] = p[k]
            rem_val = rem_val-p[k]
            k += 1
        p[k+1] = rem_val
        k += 1

def sum_41_chapter_1():
    P = int(input())
    result = next((curr for curr in next_partition(TARGET) if reduce(lambda x, y: x*y, curr) == P), [])
    return f'{len(result)} {" ".join(map(str, result))}' if result else -1

TARGET = 41
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sum_41_chapter_1()))
