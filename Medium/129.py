# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summm = 0

        def helper(node, summ):
            nonlocal summm
            if not node:
                return

            if not node.right and not node.left:
                summm += summ * 10 + node.val

            helper(node.left, summ * 10 + node.val)
            helper(node.right, summ * 10 + node.val)

        helper(root, 0)
        return summm
