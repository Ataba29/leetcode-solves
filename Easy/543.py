# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)
        curr = max(left, right)
        self.res = max(self.res, left + right)

        return curr + 1
