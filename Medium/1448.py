# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root, root.val)
        return self.res

    def helper(self, root, max_so_far):
        if not root:
            return
        if root.val >= max_so_far:
            self.res += 1
            max_so_far = root.val
        self.helper(root.left, max_so_far)
        self.helper(root.right, max_so_far)
