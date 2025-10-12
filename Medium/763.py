from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        res = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, last[c])  # extend boundary
            if i == end:  # close partition
                res.append(end - start + 1)
                start = i + 1

        return res
