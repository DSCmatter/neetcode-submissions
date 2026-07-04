# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # Cut the list into two halves
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next