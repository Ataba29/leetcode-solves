from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = len(intervals)

        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j:
                    continue

                if (
                    intervals[j][0] <= intervals[i][0]
                    and intervals[j][1] >= intervals[i][1]
                ):
                    res -= 1
                    break

        return res
