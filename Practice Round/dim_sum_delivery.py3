# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Practice Round - Problem B. Dim Sum Delivery
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/B
#
# Time:  O(1)
# Space: O(1)
#

def dim_sum_delivery():
    R, C, _, _ = map(int, input().split())
    return "YES" if R > C else "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, dim_sum_delivery()))
