# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        visited = {}

        def dfs(node: Optional["Node"]):
            if node in visited:
                return visited[node]
            clone = Node(node.val)
            visited[node] = clone
            neighbors = node.neighbors
            for nei in neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)
