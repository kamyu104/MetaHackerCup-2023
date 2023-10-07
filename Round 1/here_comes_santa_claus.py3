# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 1 - Problem A. Here Comes Santa Claus
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/A
#
# Time:  O(N)
# Space: O(1)
#

def here_comes_santa_claus():
    N = int(input())
    X = list(map(int, input().split()))
    for i in range(2):
        j = min(range(i, N), key=lambda i: X[i])
        X[i], X[j] = X[j], X[i]
    for i in range(2):
        j = max(range(2, N-i), key=lambda i: X[i])
        X[-1-i], X[j] = X[j], X[-1-i]
    return max(((X[-3]+X[-1])-(X[0]+X[1]))/2, ((X[-2]+X[-1])-(X[0]+X[2]))/2) if N == 5 else ((X[-2]+X[-1])-(X[0]+X[1]))/2

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, here_comes_santa_claus()))
