# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem D. Nearly Nim
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/D
#
# Time:  O(N)
# Space: O(N)
#

def nearly_nim():
    N = int(input())
    A = list(map(int, input().split()))
    left = [0]*(N+1)
    for i in range(N):
        left[i+1] = max(A[i]-left[i], 0)
    right = [0]*(N+1)
    for i in reversed(range(N)):
        right[i] = max(A[i]-right[i+1], 0)
    return sum(max(A[i]-left[i]-right[i+1], 0) for i in range(N))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, nearly_nim()))
