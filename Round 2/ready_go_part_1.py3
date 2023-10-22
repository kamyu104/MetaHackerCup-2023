# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 2 - Problem A1. Ready, Go (Part 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/A1
#
# Time:  O(R * C)
# Space: O(R * C)
#

def ready_go_part_1():
    def bfs(i, j):
        adj = []
        lookup[i][j] = True
        q = [(i, j)]
        while q:
            new_q = []
            for i, j in q:
                for di, dj in DIRECTIONS:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < R and 0 <= nj < C and not lookup[ni][nj]):
                        continue
                    lookup[ni][nj] = True
                    if A[ni][nj] == '.':
                        adj.append((ni, nj))
                        continue
                    new_q.append((ni, nj))
            q = new_q
        for i, j in adj:
            lookup[i][j] = False
        return len(adj) == 1

    R, C = list(map(int, input().split()))
    A = [list(input()) for _ in range(R)]
    lookup = [[A[i][j] == 'B' for j in range(C)] for i in range(R)]
    return "YES" if any(bfs(i, j) for i in range(R) for j in range(C) if A[i][j] == 'W' and not lookup[i][j]) else "NO"

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, ready_go_part_1()))
