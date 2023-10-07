# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem C1. Back in Black (Chapter 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/C1
#
# Time:  O(NlogN + Q)
# Space: O(N)
#

def back_in_black_chapter_1():
    N = int(input())
    S = list(map(int, input()))
    Q = [int(input())-1 for _ in range(int(input()))]
    cnt = [0]*N
    for x in Q:
        cnt[x] ^= 1
    for i in range(N):
        if cnt[i] == 0:
            continue
        for j in range(i, N, i+1):
            S[j] ^= 1
    result = 0
    for i in range(N):
        if S[i] == 0:
            continue
        for j in range(i, N, i+1):
            S[j] ^= 1
        result += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, back_in_black_chapter_1()))
