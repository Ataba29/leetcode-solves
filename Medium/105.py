# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mapping = {}

        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        preorder = deque(preorder)

        def build(start, end):
            if start > end:
                return None

            root = TreeNode(preorder.popleft())
            idx = mapping[root.val]

            root.left = build(start, idx - 1)
            root.right = build(idx + 1, end)

            return root

        return build(0, len(preorder) - 1)
