# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        directon = 1
        res = []
        q = deque()
        q.append(root)
        while q:
            curr = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                curr.append(node.val)
            res.append(curr[::directon])
            directon *= -1
        return res
