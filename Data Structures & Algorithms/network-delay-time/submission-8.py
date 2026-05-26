class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_m = [[float("inf")]*(n+1) for _ in range(n+1)]
        for s, f, t in times:
            adj_m[s][f] = min(adj_m[s][f], t)
        adj_m[k][k] = adj_m[k][0] = 0
        min_heap = [(adj_m[k][end], end) for end in range(1, n+1)]
        heapq.heapify(min_heap)
        visited = set()
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited: continue
            visited.add(node)
            sig = adj_m[k]
            sig[node] = min(sig[node], time)
            for next_node in range(1, n+1):
                alternate_path = sig[node]+adj_m[node][next_node]
                if sig[next_node]>alternate_path: heapq.heappush(min_heap, (alternate_path, next_node))

        return max(adj_m[k]) if max(adj_m[k])!=float("inf") else -1