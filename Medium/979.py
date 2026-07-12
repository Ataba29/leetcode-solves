from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return 0
            extraLeft = dfs(node.left)
            extraRight = dfs(node.right)
            extra = extraLeft + extraRight + node.val - 1
            res += abs(extra)
            return extra

        dfs(root)
        return res
