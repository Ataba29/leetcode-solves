# Definition for a binary tree node.
from collections import deque
import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # 1,2,3,4,5,null,6,null,null,null,null,null,null
    def serialize(self, root):
        if not root:
            return "null"
        res, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)

    def deserialize(self, data):
        if data == "null":
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q and i < len(vals):
            node = q.popleft()

            # left child
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            # right child
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root


# Create nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
print(ser.serialize(root))
ans = deser.deserialize(ser.serialize(root))
