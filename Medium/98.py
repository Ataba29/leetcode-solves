# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root, lower, upper):
        if not root:
            return True

        if not (lower < root.val < upper):
            return False

        return self.helper(root.left, lower, root.val) and self.helper(
            root.right, root.val, upper
        )
