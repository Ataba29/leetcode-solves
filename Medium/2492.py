from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))

        visited = set()
        res = float("inf")

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            nonlocal res
            for nei, dis in adj[i]:
                res = min(res, dis)
                dfs(nei)

        dfs(n)
        return int(res)


roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
n = 4
print(Solution().minScore(n, roads))
