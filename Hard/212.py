from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord("a")
            if idx not in node.children:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        res = set()
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(node, i, j, path):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            ch = board[i][j]
            idx = ord(ch) - ord("a")
            if idx not in node.children:
                return  # prune: no word in trie starts with this path

            node = node.children[idx]
            path += ch

            if node.is_end:
                res.add(path)
                node.is_end = False  # avoid duplicates

            board[i][j] = "#"  # mark visited
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(node, i + dx, j + dy, path)
            board[i][j] = ch  # backtrack

        for r in range(rows):
            for c in range(cols):
                dfs(trie, r, c, "")

        return list(res)
