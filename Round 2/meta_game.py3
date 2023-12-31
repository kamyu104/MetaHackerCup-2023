# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 2 - Problem B. Meta Game
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/B
#
# Time:  O(N)
# Space: O(1)
#

def meta_game():
    def get(i):
        i %= 2*N
        return A[i] if i < N else B[i-N]

    def check(i):
        return get(i+(N//2-1)) < get(i+N+(N//2-1))

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum(check(i) and not check(i+1) for i in range(2*N)) != 1:
        return -1
    i = next(i for i in range(2*N) if check(i) and not check(i+1))
    return i if all(get(i+j) == get(i+~j) for j in range(N)) else -1

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, meta_game()))
