from typing import List
import heapq


class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        l, r = float("inf"), 0

        for u, v, c in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, c))
            l = min(l, c)
            r = max(r, c)

        def check(mid):
            dis = [float("inf")] * n
            pq = [(0, 0)]
            dis[0] = 0

            while pq:
                d, u = heapq.heappop(pq)

                if d > k:
                    return False
                if u == n - 1:
                    return True
                if d > dis[u]:
                    continue

                for v, w in g[u]:
                    if w >= mid:
                        new_d = d + w
                        if new_d < dis[v]:
                            dis[v] = new_d
                            heapq.heappush(pq, (new_d, v))
            return False

        res = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
