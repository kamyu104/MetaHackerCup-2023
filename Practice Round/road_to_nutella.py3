# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Practice Round - Problem D. Road to Nutella
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/D
#
# Time:  O(N + M + QlogN)
# Space: O(M + NlogN)
#

from functools import partial

# template: https://github.com/kamyu104/GoogleCodeJam-Farewell-Rounds/blob/main/Round%20B/railroad_maintenance.py3
# reference: https://en.wikipedia.org/wiki/Biconnected_component
def iter_biconnected_components(graph):  # Time: O(|V| + |E|) = O(N + 2N) = O(N), Space: O(|V|) = O(N)
    def iter_biconnect(v, p):
        stk = [(1, (v, p))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                v, p = args
                index[v] = index_counter[0]
                lowlinks[v] = index_counter[0]
                index_counter[0] += 1
                stack_set.add(v)
                stack.append(v)
                stk.append((4, (v, p)))
                for w in reversed(graph[v]):
                    if w == p:
                        continue
                    stk.append((2, (w, v)))
            elif step == 2:
                w, v = args
                if w not in index:
                    stk.append((3, (w, v)))
                    stk.append((1, (w, v)))
                elif w in stack_set:
                    lowlinks[v] = min(lowlinks[v], index[w])
            elif step == 3:
                w, v = args
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif step == 4:
                v, p = args
                if lowlinks[v] == index[v]:
                    biconnected_component = []
                    w = None
                    while w != v:
                        w = stack.pop()
                        stack_set.remove(w)
                        biconnected_component.append(w)
                    bccs.append(set(biconnected_component))

    index_counter, index, lowlinks = [0], {}, {}
    stack, stack_set = [], set()
    bccs = [] 
    for v in range(len(graph)):
        if v not in index:
            iter_biconnect(v, -1)
    return bccs

# Template:
# https://github.com/kamyu104/GoogleKickStart-2021/blob/main/Round%20H/dependent_events2.py
class TreeInfos(object):  # Time: O(NlogN), Space: O(NlogN), N is the number of nodes
    def __init__(self, children, cb=lambda *x:None, cb2=lambda *x:None):  # modified
        def preprocess(curr, parent):
            # depth of the node i
            D[curr] = 1 if parent == -1 else D[parent]+1
            # ancestors of the node i
            if parent != -1:
                P[curr].append(parent)
            i = 0
            while i < len(P[curr]) and i < len(P[P[curr][i]]):
                cb(P, curr, i)
                P[curr].append(P[P[curr][i]][i])
                i += 1
            cb2(curr, parent)  # added
            # the subtree of the node i is represented by traversal index L[i]..R[i]
            C[0] += 1
            L[curr] = C[0]

        def divide(curr, parent):
            stk.append(partial(postprocess, curr))
            for i in reversed(range(len(children[curr]))):
                child = children[curr][i]
                if child == parent:
                    continue
                stk.append(partial(divide, child, curr))
            stk.append(partial(preprocess, curr, parent))

        def postprocess(curr):
            R[curr] = C[0]

        N = len(children)
        L, R, D, P, C = [0]*N, [0]*N, [0]*N, [[] for _ in range(N)], [-1]
        stk = []
        stk.append(partial(divide, 0, -1))
        while stk:
            stk.pop()()
        assert(C[0] == N-1)
        self.L, self.R, self.D, self.P = L, R, D, P

    # Template:
    # https://github.com/kamyu104/FacebookHackerCup-2019/blob/master/Final%20Round/little_boat_on_the_sea.py
    def is_ancestor(self, a, b):  # includes itself
        return self.L[a] <= self.L[b] <= self.R[b] <= self.R[a]

    def lca(self, a, b):
        if self.D[a] > self.D[b]:
            a, b = b, a
        if self.is_ancestor(a, b):
            return a
        for i in reversed(range(len(self.P[a]))):  # O(logN)
            if i < len(self.P[a]) and not self.is_ancestor(self.P[a][i], b):
                a = self.P[a][i]
        return self.P[a][0]

def calc_dist(dist, P, curr, i):
    dist[curr].append(min(dist[curr][i], dist[P[curr][i]][i]))

def min_dist(dist, tree_infos, curr, lca):  # Time: O(logN)
    result = dist[lca][0]
    for i in reversed(range(len(tree_infos.P[curr]))):  # O(logN)
        if i < len(tree_infos.P[curr]) and tree_infos.D[tree_infos.P[curr][i]] >= tree_infos.D[lca]:
            result = min(result, dist[curr][i])
            curr = tree_infos.P[curr][i]
    assert(curr == lca)
    return result

def bfs(bcc, adj, color):  # a graph is bipartite if and only if it contains no odd cycles
    root = next(iter(bcc))
    color[root] = 0
    q = [root]
    while q:
        new_q = []
        for u in q:
            for v in adj[u]:
                if v not in bcc:
                    continue
                if color[v] != -1:
                    if color[v] != color[u]^1:
                        return False  # cannot be bipartite colored
                    continue
                color[v] = color[u]^1
                new_q.append(v)
        q = new_q
    return True

def find_dist(bccs, adj, adj2):
    color = [-1]*len(adj)
    q = [i for i, bcc in enumerate(bccs) if not bfs(bcc, adj, color)]
    if not q:
        return []
    dist = [INF for _ in range(len(bccs))]
    for u in q:
        dist[u] = 0
    while q:
        new_q = []
        for u in q:
            for v in adj2[u]:
                if dist[v] != INF:
                    continue
                dist[v] = dist[u]+1
                new_q.append(v)
        q = new_q
    return [[d] for d in dist]

def road_to_nutella():
    N, M = list(map(int, input().split()))
    edges = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    Q = int(input())
    queries = [list(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    bccs = iter_biconnected_components(adj)
    lookup = [-1]*N
    for i, bcc in enumerate(bccs):
        for u in bcc:
            lookup[u] = i
    adj2 = [[] for _ in range(len(bccs))]
    for u, v in edges:
        nu, nv = lookup[u], lookup[v]
        if nu == nv:
            continue
        adj2[nu].append(nv)
        adj2[nv].append(nu)
    dist = find_dist(bccs, adj, adj2)
    if not dist:
        return -1*len(queries)
    tree_infos = TreeInfos(adj2, cb=partial(calc_dist, dist))
    result = 0
    for a, b in queries:
        u, v = lookup[a], lookup[b]
        lca = tree_infos.lca(u, v)
        result += min(min_dist(dist, tree_infos, u, lca), min_dist(dist, tree_infos, v, lca))
    return result

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, road_to_nutella()))
