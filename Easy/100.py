# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p == None) != (q == None):
            return False
        if p.val != q.val:
            return False
        return (
            True
            and self.isSameTree(p.right, q.right)
            and self.isSameTree(p.left, q.left)
        )
