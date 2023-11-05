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
        lookup = [[0]*2 for _ in range(N)]
        for u in reversed(range(N)):
            result = max(result, sum(lookup[u]))
            if u-1 < 0:
                break
            v = P[u-1]
            tmp = lookup[u][0]+1
            for i in range(2):
                if tmp > lookup[v][i]:
                    lookup[v][i], tmp = tmp, lookup[v][i]
        return result

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    d = tree_diameter()
    return (N+(N-d))*(d+1)//2 % MOD

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, similar_ships()))