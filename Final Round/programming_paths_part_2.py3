# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem A2. Programming Paths (Part 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/A2
#
# Time:  precompute: O(R * C + K^2 * D)
#        runtime:    O(R * C)
# Space: O(R * C + K^2)
#

def op(A, B, D, P):
    if D == 0 and P == 0:
        A += 1
    elif D == 0 and P == 1:
        B += A
    elif D == 1 and P == 0:
        A -= 1
    elif D == 1 and P == 1:
        A = B
    return A, B

def bfs(G, extend=lambda: None, add=lambda r, c: None):
    R, C = len(G), len(G[0])
    r, c = next((r, c) for r in range(R) for c in range(C) if G[r][c] == '@')
    cnts = [[0]*C for _ in range(R)]
    cnts[r][c] = 1
    depths = [[(r, c)]]
    lookup = [[-1]*C for _ in range(R)]
    lookup[r][c] = len(depths)-1
    extend()
    while depths[-1]:
        depths.append([])
        extend()
        for r, c in depths[-2]:
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < R and 0 <= nc < C and G[nr][nc] != '#'):
                    continue
                if lookup[nr][nc] == -1 or lookup[nr][nc] == len(depths)-1:
                    cnts[nr][nc] += cnts[r][c]
                if lookup[nr][nc] != -1:
                    continue
                lookup[nr][nc] = len(depths)-1
                add(nr, nc)
                depths[-1].append((nr, nc))
    return depths, cnts

def check(G, K):
    def extend():
        ops.append([])

    def add(r, c):
        if G[r][c] == '*':
            ops[-1].append((r, c))

    ops = []
    _, cnts = bfs(G, extend, add)
    A = B = 0
    for d in range(len(ops)):
        if not ops[d]:
            continue
        A, B = op(A, B, d%2, sum(cnts[r][c] for r, c in ops[d])%2)
    assert(A == K)

def backtracing(K):
    result = [list(row) for row in G]
    curr = DP[K, K]
    while curr:
        idxs, prev = curr
        for r, c in idxs:
            result[r][c] = '*'
        curr = DP[prev]
    return result

def programming_paths_part_2():
    K = int(input())
    result = backtracing(K)
    return "%s %s\n%s" % (R, C, "\n".join(map(lambda x: "".join(x), result)))

def precompute():
    depths, cnts = bfs(G)
    dp = {(0, 0):None}
    q = [(0, 0)]
    d = 0
    while q:
        d += 1
        if not depths[d]:
            break
        new_q = []
        for A, B in q:
            new_q.append((A, B))
            for p in range(1, min(len(depths[d]), 2)+1):
                idxs = depths[d][:p]
                assert(sum(cnts[r][c] for r, c in idxs)%2 == p%2)
                new_A_B = op(A, B, d%2, p%2)
                if not (0 <= new_A_B[0] <= MAX_K and 0 <= new_A_B[1] <= MAX_K and new_A_B not in dp):
                    continue
                dp[new_A_B] = (idxs, (A, B))
                new_q.append(new_A_B)
        q = new_q
    return dp

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
G = [
    "@.....#.#.",
    "#.#.#.#...",
    ".#.#..#.#.",
    ".....#..#.",
    "#.#.#..##.",
    "...#.#.#..",
    ".#.#.#..#.",
    "..#...#.#.",
    "#...#....#",
    "..#..#.#..",
]
R, C = len(G), len(G[0])
MAX_K = 10000
DP = precompute()
for K in range(MAX_K+1):
    check(backtracing(K), K)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, programming_paths_part_2()))
