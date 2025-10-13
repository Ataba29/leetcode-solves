from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort balloons by their ending coordinate
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]

        for x_start, x_end in points[1:]:
            if x_start > end:
                # Need a new arrow
                arrows += 1
                end = x_end  # update arrow position

        return arrows
