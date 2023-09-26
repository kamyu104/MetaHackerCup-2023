# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Practice Round - Problem A. Cheeseburger Corollary 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/A1
#
# Time:  O(1)
# Space: O(1)
#

def cheeseburger_corollary_1(): 
    S, D, K = map(int, input().split())
    return "YES" if S*2+D*2 >= K+1 and S+D*2 >= K else "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cheeseburger_corollary_1()))
