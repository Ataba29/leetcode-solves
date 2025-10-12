# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def helper(root):
            nonlocal max_sum

            if not root:
                return 0

            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)

            max_sum = max(max_sum, left + right + root.val)

            return root.val + max(left, right)

        helper(root)
        return max_sum
