# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            new_t = curr.next
            curr.next = prev
            prev = curr
            curr = new_t
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
