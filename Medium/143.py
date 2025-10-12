# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head
        # get to middle of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
        # now merge both halfs in desired order
        x = head
        y = prev
        while y:
            tempOne = x.next
            tempSec = y.next
            x.next = y
            y.next = tempOne
            x = tempOne
            y = tempSec
