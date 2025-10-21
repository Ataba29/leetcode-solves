from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookups
        mapping = {val: i for i, val in enumerate(inorder)}

        postorder = deque(postorder)

        def build(start, end):
            if start > end:
                return None

            # The last element in postorder is the root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Find the index of the root in inorder
            idx = mapping[root_val]

            # Build right subtree first (because of postorder's order)
            root.right = build(idx + 1, end)
            root.left = build(start, idx - 1)

            return root

        return build(0, len(inorder) - 1)
