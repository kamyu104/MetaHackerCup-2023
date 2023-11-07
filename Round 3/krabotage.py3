# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem C. Krab-otage
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/C
#
# Time:  O(R * C * (R + C))
# Space: O(R * C)
#

def krabotage():
    R, C = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(R)]
    dp_l = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            dp_l[r][c] = A[r][c]+max(dp_l[r-1][c] if r-1 >= 0 else 0, dp_l[r][c-1] if c-1 >= 0 else 0)
    dp_r = [[0]*C for _ in range(R)]
    for r in reversed(range(R)):
        for c in reversed(range(C)):
            dp_r[r][c] = A[r][c]+max(dp_r[r+1][c] if r+1 < R else 0, dp_r[r][c+1] if c+1 < C else 0)
    dp_h, dp_v = [[[dp_r[0][0]]*C for _ in range(R)] for _ in range(2)]
    for r in reversed(range(R)):
        for c in range(C):
            accu = 0
            for nc in reversed(range(c+1)):
                left = (dp_l[r-1][nc+1] if nc+1 <= c else dp_l[r-1][nc]) if r-1 >= 0 else 0
                right = max(dp_r[r][c+2] if c+2 < C else 0, dp_r[r+1][nc+1] if r+1 < R and nc+1 < C else 0)
                dp_h[r][c] = min(dp_h[r][c], max(accu, max(left, dp_l[r][nc-1] if nc-1 >= 0 else 0)+right, dp_v[r+1][nc] if r+1 < R else 0))
                accu = max(accu, left+right)
            accu = 0
            for nr in range(r, R):
                left = max(dp_l[r-2][c] if r-2 >= 0 else 0, dp_l[nr-1][c-1] if nr-1 >= 0 and c-1 >= 0 else 0)
                right = (dp_r[nr-1][c+1] if nr-1 >= r else dp_r[nr][c+1]) if c+1 < C else 0
                dp_v[r][c] = min(dp_v[r][c], max(accu, left+max(right, dp_r[nr+1][c] if nr+1 < R else 0), dp_h[nr][c-1] if c-1 >= 0 else 0))
                accu = max(accu, left+right)
    assert(dp_h[0][C-1] == dp_v[0][C-1])
    return dp_h[0][C-1]

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, krabotage()))
