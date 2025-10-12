# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        mapp = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            mapp[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = mapp[curr]
            copy.next = mapp[curr.next]
            copy.random = mapp[curr.random]
            curr = curr.next

        return mapp[head]
