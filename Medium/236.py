# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        ans = None

        def helper(node):
            nonlocal ans
            if not node:
                return False
            foundFirst = helper(node.left)
            foundSecond = helper(node.right)

            if (foundFirst and foundSecond) or (
                (foundFirst or foundSecond) and (node == p or node == q)
            ):
                ans = node
                return True
            return foundFirst or foundSecond or (node == p or node == q)

        helper(root)
        return ans
