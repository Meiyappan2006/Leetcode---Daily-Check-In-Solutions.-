class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def bfs_parity(n, edges):
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v); g[v].append(u)
            parity, visited = [0] * n, [False] * n
            count, dq = [0, 0], deque([0])
            visited[0] = True
            count[0] = 1
            while dq:
                u = dq.popleft()
                pu = parity[u]
                for w in g[u]:
                    if not visited[w]:
                        visited[w] = True
                        pw = pu ^ 1
                        parity[w] = pw
                        count[pw] += 1
                        dq.append(w)
            return parity, count

        n, m = len(edges1) + 1, len(edges2) + 1
        p1, c1 = bfs_parity(n, edges1)  # parity & count for Tree1
        p2, c2 = bfs_parity(m, edges2)  # parity & count for Tree2
        max_odd2 = max(c2[0], c2[1])
        return [c1[p1[u]] + max_odd2 for u in range(n)]

        def build_tree(n, edges):
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        def get_tree_data(n, g):
            depths = [-1] * n
            dq = collections.deque()
            depths[0] = 0
            dq.append((0, 0))    # u, depth
            visited = {0}
            total_even_nodes = 0
            total_odd_nodes = 0
            while dq:
                u_curr, depth = dq.popleft()
                if depth % 2 == 0:
                    total_even_nodes += 1
                else:
                    total_odd_nodes += 1
                for w in g[u_curr]:
                    if w not in visited:
                        visited.add(w)
                        depths[w] = depth + 1
                        dq.append((w, depth + 1))
            return total_even_nodes, total_odd_nodes, depths

        n, m = len(edges1) + 1, len(edges2) + 1
        tree1 = build_tree(n, edges1)
        tree2 = build_tree(m, edges2)
        t1_even, t1_odd, t1_depths = get_tree_data(n, tree1)
        t2_even, t2_odd, _         = get_tree_data(m, tree2)
        even1 = [0] * n
        for u in range(n):
            if t1_depths[u] % 2 == 0:   even1[u] = t1_even
            else:                       even1[u] = t1_odd
        max_odd2 = max(t2_even, t2_odd)
        answer = [0] * n
        for u in range(n):
            answer[u] = even1[u] + max_odd2
        return answer
