# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []

        def dfs(node):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        dfs(root)
        return res
