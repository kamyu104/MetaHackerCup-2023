# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Final Round - Problem B. Transposing Tiles
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/B
#
# Time:  O(R * C * 2 * (2 * L + 1)^2 * 2 * ((((L - 1) + 2) * 2)) * 2) = O(R * C * 3136)
# Space: O(R * C + ((((L - 1) + 2) * 2)) * 2) = O(R * C + 16)
#

from collections import Counter

def transposing_tiles():
    def check(r, c):
        return 0 <= r < R and 0 <= c < C

    def watch(candidates, r, c, d):
        candidates[r, c] += d
        if not candidates[r, c]:
            del candidates[r, c]
        for nr in range(max(r-L+1, 0), r):
            candidates[nr, c] += d
            if not candidates[nr, c]:
                del candidates[nr, c]
        for nc in range(max(c-L+1, 0), c):
            candidates[r, nc] += d
            if not candidates[r, nc]:
                del candidates[r, nc]

    def count(candidates):
        assert(len(candidates) <= MAX_SCORE_BY_TWO_MOVES)
        return (sum(G[r][c] == G[r+1][c] == G[r+2][c] if r+2 < R else 0 for r, c in candidates.keys())+
                sum(G[r][c] == G[r][c+1] == G[r][c+2] if c+2 < C else 0 for r, c in candidates.keys()))

    R, C = list(map(int, input().split()))
    G = [list(map(int, input().split())) for _ in range(R)]
    dp = [[0]*C for _ in range(R)]
    cnt = [0]
    candidates = Counter()
    for r in range(R):
        for c in range(C):
            watch(candidates, r, c, +1)
            for nr, nc in ((r+1, c), (r, c+1)):
                if not check(nr, nc) or G[nr][nc] == G[r][c]:
                    continue
                G[r][c], G[nr][nc] = G[nr][nc], G[r][c]
                watch(candidates, nr, nc, +1)
                dp[r][c] = max(dp[r][c], count(candidates))
                watch(candidates, nr, nc, -1)
                G[r][c], G[nr][nc] = G[nr][nc], G[r][c]
            watch(candidates, r, c, -1)
            while not dp[r][c] < len(cnt):
                cnt.append(0)
            cnt[dp[r][c]] += 1
    assert(len(cnt) <= MAX_SCORE_BY_ONE_MOVE+1)
    max_cnt = next((i for i in reversed(range(len(cnt))) if cnt[i]), 0)
    result = 0
    for r1 in range(R):
        for c1 in range(C):
            if dp[r1][c1]+MAX_SCORE_BY_ONE_MOVE <= result:
                continue
            for r2 in range(max(r1-L, 0), min((r1+L)+1, R)):
                for c2 in range(max(c1-L, 0), min((c1+L)+1, C)):
                    cnt[dp[r2][c2]] -= 1
            result = max(result, next((i for i in reversed(range(max_cnt+1)) if cnt[i]), 0)+dp[r1][c1])
            if result == MAX_SCORE_BY_TWO_MOVES:
                return result
            watch(candidates, r1, c1, +1)
            for nr1, nc1 in ((r1+1, c1), (r1, c1+1)):
                if not check(nr1, nc1) or G[nr1][nc1] == G[r1][c1]:
                    continue
                G[r1][c1], G[nr1][nc1] = G[nr1][nc1], G[r1][c1]
                watch(candidates, nr1, nc1, +1)
                for r2 in range(max(r1-L, 0), min((r1+L)+1, R)):
                    for c2 in range(max(c1-L, 0), min((c1+L)+1, C)):
                        watch(candidates, r2, c2, +1)
                        for nr2, nc2 in ((r2+1, c2), (r2, c2+1)):
                            if not check(nr2, nc2) or G[nr2][nc2] == G[r2][c2]:
                                continue
                            G[r2][c2], G[nr2][nc2] = G[nr2][nc2], G[r2][c2]
                            watch(candidates, nr2, nc2, +1)
                            result = max(result, count(candidates))
                            if result == MAX_SCORE_BY_TWO_MOVES:
                                return result
                            watch(candidates, nr2, nc2, -1)
                            G[r2][c2], G[nr2][nc2] = G[nr2][nc2], G[r2][c2]
                        watch(candidates, r2, c2, -1)
                watch(candidates, nr1, nc1, -1)
                G[r1][c1], G[nr1][nc1] = G[nr1][nc1], G[r1][c1]
            watch(candidates, r1, c1, -1)
            for r2 in range(max(r1-L, 0), min((r1+L)+1, R)):
                for c2 in range(max(c1-L, 0), min((c1+L)+1, C)):
                    cnt[dp[r2][c2]] += 1
    return result

L = 3
MAX_SCORE_BY_ONE_MOVE = ((L-1)+2)*2
MAX_SCORE_BY_TWO_MOVES = MAX_SCORE_BY_ONE_MOVE*2
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, transposing_tiles()))
