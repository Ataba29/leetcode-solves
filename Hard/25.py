# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, start: ListNode, end: ListNode) -> ListNode:
        prev, curr = end, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # find kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # not enough nodes left

            group_next = kth.next
            # reverse this group
            new_head = self.reverse(group_prev.next, group_next)

            # reconnect
            old_head = group_prev.next
            group_prev.next = new_head
            group_prev = old_head
