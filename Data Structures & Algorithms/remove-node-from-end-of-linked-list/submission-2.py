# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass
        # first pass: traverse the list 
        length = 0 
        curr = head 

        while curr:
            length += 1 
            curr = curr.next 

        # if the node to remove is head simply return the next node 
        if length == n:
            return head.next 

        # second pass: move to the node just before the one we want to remove 
        curr = head 
        for _ in range(length - n - 1):
            curr = curr.next 

        # skip the target node and update the curr ptr
        curr.next = curr.next.next 

        return head


