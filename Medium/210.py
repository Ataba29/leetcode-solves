from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        cycle = set()
        preq = defaultdict(list)

        for crs, pre in prerequisites:
            preq[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in preq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
