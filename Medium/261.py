from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            parx, pary = find(x), find(y)
            if parx == pary:
                return False
            if rank[parx] < rank[pary]:
                par[parx] = pary
                rank[pary] += rank[parx]
            else:
                par[pary] = parx
                rank[parx] += rank[pary]
            return True

        for v, w in edges:
            if not union(v, w):
                return False

        return len(set([find(i) for i in range(n)])) == 1
