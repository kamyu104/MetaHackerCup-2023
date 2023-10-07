# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem C2. Back in Black (Chapter 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/C2
#
# Time:  O(NlogN)
# Space: O(N)
#

def back_in_black_chapter_2():
    N = int(input())
    S = list(map(int, input()))
    Q = [int(input())-1 for _ in range(int(input()))]
    cnt = [0]*N
    for i in range(N):
        if S[i] == 0:
            continue
        for j in range(i, N, i+1):
            S[j] ^= 1
        cnt[i] = 1
    result = 0
    curr = sum(cnt)
    for x in Q:
        curr += 1 if not cnt[x] else -1
        cnt[x] ^= 1
        result += curr
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, back_in_black_chapter_2()))
