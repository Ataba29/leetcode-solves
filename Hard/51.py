from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()  # columns with queens
        diag1 = set()  # r - c (top-left to bottom-right)
        diag2 = set()  # r + c (top-right to bottom-left)

        def backtrack(row: int):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # remove queen
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res
