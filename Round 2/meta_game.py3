# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 2 - Problem B. Meta Game
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/B
#
# Time:  O(N)
# Space: O(N)
#

def meta_game():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_B = A+B
    for i in range(len(A_B)):
        if not (A_B[(i+(N//2-1))%len(A_B)] < A_B[(i+N+(N//2-1))%len(A_B)] and A_B[((i+1)+(N//2-1))%len(A_B)] >= A_B[((i+1)+N+(N//2-1))%len(A_B)]):
            continue
        if all(A_B[(i+j)%len(A_B)] < A_B[(i+N+j)%len(A_B)] for j in range(N//2)) and all(A_B[(i+j)%len(A_B)] == A_B[((i-1)-j)%len(A_B)] for j in range(N)):
            return i
        break
    return -1

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, meta_game()))
