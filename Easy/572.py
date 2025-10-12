# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val:
            self.res = self.res or self.help(root, subRoot)
        return (
            self.res
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def help(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (root == None) != (subRoot == None):
            return False
        if root.val != subRoot.val:
            return False
        return (
            True
            and self.help(root.left, subRoot.left)
            and self.help(root.right, subRoot.right)
        )
