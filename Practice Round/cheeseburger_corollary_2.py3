# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Practice Round - Problem A. Cheeseburger Corollary 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/A2
#
# Time:  O(1)
# Space: O(1)
#

def cheeseburger_corollary_2():
    def count(S, D):
        return S+D*2-int(S == 0) if D >= 0 else 0

    A, B, C = map(int, input().split())
    return max(count(0, C//B), count(1, (C-A)//B), count(2, (C-2*A)//B), count(C//A, 0))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cheeseburger_corollary_2()))
