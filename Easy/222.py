# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.countLeft(root)
        right = self.countRight(root)

        if left == right:
            return 2**left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countLeft(self, node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def countRight(self, node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h
