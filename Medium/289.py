from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbors += 1

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 2
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 3

        for r in range(rows):
            for c in range(cols):
                board[r][c] %= 2
