# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Practice Round - Problem D. Road to Nutella
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/D
#
# Time:  O(N + M + Q + NlogN + QlogQ)
# Space: O(N + M + Q)
#

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

class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.rank = [0]*n
        self.group = [set() for _ in range(n)]  # added

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return 0  # modified
        if self.rank[x] > self.rank[y]:  # union by rank
            x, y = y, x
        self.set[x] = self.set[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        # added below
        if len(self.group[x]) > len(self.group[y]):  # move from smaller group to bigger one, total time: O(QlogQ)
            self.group[x], self.group[y] = self.group[y], self.group[x]
        result = 0
        for i in self.group[x]:
            if i not in self.group[y]:
                self.group[y].add(i)
            else:
                self.group[y].remove(i)
                result += 1
        self.group[x].clear()
        return result  # modified

    def group_add(self, u, i):
        self.group[u].add(i)

def is_bipartite(bcc, adj, color):  # a graph is bipartite if and only if it contains no odd cycles
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
    q = [i for i, bcc in enumerate(bccs) if not is_bipartite(bcc, adj, color)]
    if not q:
        return []
    dist = [-1 for _ in range(len(bccs))]
    for u in q:
        dist[u] = 0
    while q:
        new_q = []
        for u in q:
            for v in adj2[u]:
                if dist[v] != -1:
                    continue
                dist[v] = dist[u]+1
                new_q.append(v)
        q = new_q
    return dist

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
    uf = UnionFind(len(adj2))
    result = 0
    for i, (a, b) in enumerate(queries):
        u, v = lookup[a], lookup[b]
        if u == v:
            result += dist[u]
        else:
            uf.group_add(u, i)
            uf.group_add(v, i)
    lookup2 = [0]*len(adj2)
    idxs = list(range(len(adj2)))
    idxs.sort(key=lambda x: dist[x], reverse=True)  # Time: O(NlogN)
    for u in idxs:
        lookup2[u] = True
        for v in adj2[u]:
            if lookup2[v]:
                result += uf.union_set(u, v)*dist[u]
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, road_to_nutella()))
