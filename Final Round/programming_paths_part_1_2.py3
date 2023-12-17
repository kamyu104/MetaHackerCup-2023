# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem A1. Programming Paths (Part 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/A1
#
# Time:  precompute: O(R * C)
#        runtime:    O(R * C)
# Space: O(R * C)
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
                depths[-1].append((nr, nc))
                add(nr, nc)
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
    return A == K

def build(K):
    def fill(D, cnt):
        assert(d[0] < len(DEPTHS) and d[0]%2 == D and len(DEPTHS[d[0]]) >= cnt)
        for r, c in DEPTHS[d[0]][:cnt]:
            result[r][c] = '*'
        d[0] += 1

    def double_plus_zero():
        fill(0, 1)
        fill(1, 1)

    def double_plus_one():
        fill(0, 2)
        fill(1, 0)
        fill(0, 1)
        fill(1, 1)

    def double_minus_one():
        fill(0, 0)
        fill(1, 2)
        fill(0, 1)
        fill(1, 1)

    result = [list(row) for row in G]
    d = [2]
    def iter_dfs(x):
        stk = [(1, (x,))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                x = args[0]
                if x == 0:
                    double_plus_zero()
                    continue
                if x == 1:
                    double_plus_one()
                    continue
                if x%2 == 0:
                    stk.append((2, (double_plus_zero,)))
                    stk.append((1, (x//2,)))
                    continue
                if x%4 == 1:
                    stk.append((2, (double_plus_zero, double_plus_one)))
                    stk.append((1, (x//4,)))
                    continue
                if x%4 == 3:
                    stk.append((2, (double_plus_zero, double_minus_one)))
                    stk.append((1, (x//4+1,)))
                    continue
            elif step == 2:
                for fn in args:
                    fn()

    iter_dfs(K)
    return result

def programming_paths_part_1():
    K = int(input())
    result = build(K)
    return "%s %s\n%s" % (R, C, "\n".join(map(lambda x: "".join(x), result)))

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
G = [
    ".#...#...#...",
    ".#.#.#.#.#.#.",
    ".#.#.#.#.#.#.",
    ".#.#.#.#.#.#.",
    ".#.#.#.#.#.#.",
    ".#.#.#.#.#.#.",
    ".#.#.#@#.#.#.",
    ".#.#.#.#.#.#.",
    ".#.#.#.#.#.#.",
    ".#.#.#.#.#.#.",
    ".#.#.#.#.#.#.",
    ".#.#.#.#.#.#.",
    "...#...#...#.",
]
R, C = len(G), len(G[0])
MAX_K = 10000
DEPTHS, CNTS = bfs(G)
assert(all(CNTS[r][c] == 1 for candidates in DEPTHS for r, c in candidates))
assert(all(len(candidates) == 2 for candidates in DEPTHS[1:-1]))
for K in range(MAX_K+1):
    assert(check(build(K), K))
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, programming_paths_part_1()))
