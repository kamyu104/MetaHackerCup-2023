# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Practice Round - Problem C. Two Apples a Day
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/C
#
# Time:  O(NlogN)
# Space: O(1)
#

from bisect import insort_left

def two_apples_a_day():
    INF = float("inf")
    def f(x):
        v = x*N-total
        if v <= 0:
            return INF
        insort_left(A, v)
        result = v if all(A[i]+A[~i] == x for i in range(N)) else INF
        A.remove(v)
        return result
        
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N == 1:
        return 1
    total = sum(A)
    result = min(f(A[0]+A[-1]), f(A[0]+A[-2]), f(A[1]+A[-1]))
    return result if result != INF else -1

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, two_apples_a_day()))
