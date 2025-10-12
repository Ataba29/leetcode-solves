from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe = set()
        rows = len(board)
        cols = len(board[0])

        def dfsSafe(x, y):
            if (
                x >= rows
                or y >= cols
                or x < 0
                or y < 0
                or board[x][y] == "X"
                or (x, y) in safe
            ):
                return
            safe.add((x, y))
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfsSafe(x + dx, y + dy)

        for r in range(rows):
            if board[r][0] == "O":
                dfsSafe(r, 0)
            if board[r][cols - 1] == "O":
                dfsSafe(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfsSafe(0, c)
            if board[rows - 1][c] == "O":
                dfsSafe(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"
