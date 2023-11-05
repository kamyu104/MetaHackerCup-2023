# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem E. Similar Ships
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/E
#
# Time:  O(N)
# Space: O(N)
#

def similar_ships():
    def tree_diameter():
        result = 0
        dp = [[0]*2 for _ in range(N)]
        for u in reversed(range(1, N)):
            v = P[u-1]
            tmp = dp[u][0]+1
            if tmp > dp[v][0]:
                dp[v][0], tmp = tmp, dp[v][0]
            if tmp > dp[v][1]:
                dp[v][1], tmp = tmp, dp[v][1]
            result = max(result, dp[v][0]+dp[v][1])
        return result

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    d = tree_diameter()
    return (N+(N-d))*(d+1)//2 % MOD

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, similar_ships()))
