from typing import List


class Solution:

    def backtrack(
        self, board: List[List[str]], r: int, c: int, word: str, idx: int
    ) -> bool:
        if idx == len(word):
            return True
        if (
            r >= len(board)
            or r < 0
            or c >= len(board[0])
            or c < 0
            or board[r][c] == "#"
        ):
            return False

        ch = board[r][c]
        res = False
        if ch != word[idx]:
            return False
        board[r][c] = "#"
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            res = res or self.backtrack(board, r + dx, c + dy, word, idx + 1)
        board[r][c] = ch
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if self.backtrack(board, r, c, word, 0):
                        return True

        return False
