class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [-1] * n
        d, curr = 0, node1
        while curr != -1 and dist1[curr] == -1:
            dist1[curr] = d
            d += 1
            curr = edges[curr]

        dist2, d, curr = [-1] * n, 0, node2
        while curr != -1 and dist2[curr] == -1:
            dist2[curr] = d
            d += 1
            curr = edges[curr]

        res, best = -1, float('inf')
        for i in range(n):
            if dist1[i] >= 0 and dist2[i] >= 0:
                m = max(dist1[i], dist2[i])
                if m < best:
                    best, res = m, i
        return res
