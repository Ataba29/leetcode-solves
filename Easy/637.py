# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        q = deque()
        q.append(root)
        while q:
            summ = 0
            length = len(q)
            for i in range(length):
                node = q.popleft()
                summ += node.val
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            res.append(summ / length)
        return res
