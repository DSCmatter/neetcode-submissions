# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative method 
        prev, curr = None, head

        while curr:
            temp = curr.next # saving the removed ptrs
            curr.next = prev 
            prev = curr 
            curr = temp
        return prev
