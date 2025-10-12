from typing import List


class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) in self.points:
            self.points[(point[0], point[1])] += 1
        else:
            self.points[(point[0], point[1])] = 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (px, py), cnt in self.points.items():
            # Only consider points in the same column
            if px == x and py != y:
                side_len = y - py  # distance between y coordinates

                # Check the other two corners for a square to the right
                if (x + side_len, y) in self.points and (
                    x + side_len,
                    py,
                ) in self.points:
                    total += (
                        cnt
                        * self.points[(x + side_len, y)]
                        * self.points[(x + side_len, py)]
                    )

                # Check the other two corners for a square to the left
                if (x - side_len, y) in self.points and (
                    x - side_len,
                    py,
                ) in self.points:
                    total += (
                        cnt
                        * self.points[(x - side_len, y)]
                        * self.points[(x - side_len, py)]
                    )

        return total


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
