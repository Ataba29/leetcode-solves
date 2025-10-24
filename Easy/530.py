# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inres = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inres.append(node.val)
            inorder(node.right)

        inorder(root)
        inres[::-1]
        res = inres[1] - inres[0]
        for i in range(1, len(inres)):
            res = min(inres[i] - inres[i - 1], res)
        return res
