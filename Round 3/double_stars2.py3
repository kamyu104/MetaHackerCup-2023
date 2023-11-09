# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem D. Double Stars
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/D
#
# Time:  O(N)
# Space: O(N)
#

def inplace_counting_sort(idxs, cb, reverse=False):  # Time: O(n)
    if not idxs:
        return
    count = [0]*(max(cb(idx) for idx in idxs)+1)
    for idx in idxs:
        count[cb(idx)] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    for i in reversed(range(len(idxs))):  # inplace but unstable sort
        while idxs[i] >= 0:
            count[cb(idxs[i])] -= 1
            j = count[cb(idxs[i])]
            idxs[i], idxs[j] = idxs[j], ~idxs[i]
    for i in range(len(idxs)):
        idxs[i] = ~idxs[i]  # restore values
    if reverse:  # unstable sort
        idxs.reverse()

def double_stars():
    def bfs():
        cnt = [0]*N
        dp_down = [0]*N
        q = [u for u in range(N) if cnt[u] == len(adj[u])]
        while q:
            new_q = []
            for u in q:
                if u == 0:
                    continue
                v = P[u-1]
                dp_down[v] = max(dp_down[v], dp_down[u]+1)
                cnt[v] += 1
                if cnt[v] == len(adj[v]):
                    new_q.append(v)
            q = new_q
        return dp_down

    def bfs2():
        dp_up = [0]*N
        q = [0]
        while q:
            new_q = []
            for u in q:
                prefix = [-1]*(len(adj[u])+1)
                for i in range(len(adj[u])):
                    prefix[i+1] = max(prefix[i], dp_down[adj[u][i]])
                suffix = [-1]*(len(adj[u])+1)
                for i in reversed(range(len(adj[u]))):
                    suffix[i] = max(suffix[i+1], dp_down[adj[u][i]])
                for i, v in enumerate(adj[u]):
                    dp_up[v] = max(dp_up[u], prefix[i]+1, suffix[i+1]+1)+1
                    new_q.append(v)
            q = new_q
        return dp_up

    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    adj = [[] for _ in range(N)]
    for u, v in enumerate(P, 1):
        adj[v].append(u)
    dp_down = bfs()
    dp_up = bfs2()
    dists = [[] for _ in range(N)]
    for u, v in enumerate(P, 1):
        dists[u].append(dp_up[u])
        dists[v].append(dp_down[u]+1)
    dist_pairs = [(d, u) for u in range(N) for d in dists[u]]
    idxs = list(range(len(dist_pairs)))
    inplace_counting_sort(idxs, lambda x: dist_pairs[x][0])
    sorted_dists = [[] for _ in range(N)]
    for i in reversed(idxs):
        sorted_dists[dist_pairs[i][1]].append(dist_pairs[i][0])
    result = 0
    debug_cnt = 0
    for u, v in enumerate(P, 1):
        found1 = found2 = False
        i = j = 0
        for _ in range(min(len(sorted_dists[u]), len(sorted_dists[v]))-1):
            debug_cnt += 1
            if not found1 and sorted_dists[u][i] == dp_up[u]:
                found1 = True
                i += 1
            if not found2 and sorted_dists[v][j] == dp_down[u]+1:
                found2 = True
                j += 1
            result += min(sorted_dists[u][i], sorted_dists[v][j])
            i += 1
            j += 1
    assert(debug_cnt <= (N-1)-1)
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, double_stars()))
