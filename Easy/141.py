# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        bunny = head
        tort = head

        while bunny and bunny.next:
            tort = tort.next
            bunny = bunny.next.next
            if bunny == tort:
                return True
        return False
