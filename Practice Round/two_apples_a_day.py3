# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Practice Round - Problem C. Two Apples a Day
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/C
#
# Time:  O(NlogN)
# Space: O(1)
#

def two_apples_a_day():
    INF = float("inf")
    def find_missing(target):
        result = 0
        left, right = 0, len(A)-1
        while left <= right:
            if A[left]+A[right] == target:
                if left == right:
                    assert(result == 0)
                    result = target//2
                left += 1
                right -= 1
                continue
            if result:
                 return INF
            if A[left]+A[right] < target:
                result = target-A[left]
                left += 1
            else:
                result = target-A[right]
                right -= 1
            if result <= 0:
                return INF
        return result
        
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N == 1:
        return 1
    result = min(find_missing(A[0]+A[-1]), find_missing(A[0]+A[-2]), find_missing(A[1]+A[-1]))
    return result if result != INF else -1

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, two_apples_a_day()))
