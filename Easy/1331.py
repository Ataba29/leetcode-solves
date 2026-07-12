from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique = sorted(set(arr))

        rank = {}
        for idx, val in enumerate(unique):
            rank[val] = idx + 1

        return [rank[x] for x in arr]
