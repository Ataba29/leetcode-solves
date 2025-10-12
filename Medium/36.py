from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    continue

                if val in row[r] or val in col[c] or val in boxes[(r // 3, c // 3)]:
                    return False

                row[r].add(val)
                col[c].add(val)
                boxes[(r // 3, c // 3)].add(val)

        return True
