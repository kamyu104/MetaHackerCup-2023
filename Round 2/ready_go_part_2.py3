# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 2 - Problem A2. Ready, Go (Part 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/A2
#
# Time:  O(R * C)
# Space: O(R * C)
#

def ready_go_part_2():
    def bfs(i, j):
        cnt = 0
        adj = []
        lookup[i][j] = True
        q = [(i, j)]
        while q:
            new_q = []
            for i, j in q:
                cnt += 1
                for di, dj in DIRECTIONS:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < R and 0 <= nj < C and A[ni][nj] in ".W" and not lookup[ni][nj]):
                        continue
                    lookup[ni][nj] = True
                    if A[ni][nj] == '.' :
                        adj.append((ni, nj))
                        continue
                    lookup[ni][nj] = True
                    new_q.append((ni, nj))
            q = new_q
        for i, j in adj:
            lookup[i][j] = False
        if len(adj) == 1:
            i, j = adj[0]
            dp[i][j] += cnt

    R, C = list(map(int, input().split()))
    A = [list(input()) for _ in range(R)]
    dp = [[0]*C for _ in range(R)]
    lookup = [[False]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j] == 'W' and not lookup[i][j]:
                bfs(i, j)
    return max(max(row) for row in dp)

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, ready_go_part_2()))
