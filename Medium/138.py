# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        or_to_new = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            or_to_new[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = or_to_new[curr]
            copy.next = or_to_new[curr.next]
            copy.random = or_to_new[curr.random]
            curr = curr.next
        return or_to_new[head]
