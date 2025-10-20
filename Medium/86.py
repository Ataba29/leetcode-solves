# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        big = ListNode(0, None)
        bigcurr = big
        prev = dummy
        curr = dummy.next
        while curr:
            if curr.val >= x:
                prev.next = curr.next
                curr.next = None
                bigcurr.next = curr
                bigcurr = bigcurr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        prev.next = big.next
        return dummy.next
