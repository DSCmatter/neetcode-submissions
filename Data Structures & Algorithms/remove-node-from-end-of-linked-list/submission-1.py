# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two ptrs + dummynode
        dummy = ListNode(0, head)
        l = dummy 
        r = head 

        while n > 0 and r: # move r forward by n steps 
            r = r.next 
            n -= 1 # once n = 0 means weve shifted by the amount that we wanted to shift by 
        
        # shift both ptrs till right reaches end
        while r:
            l = l.next  
            r = r.next

        # delete and update ptrs
        # Now left.next is the node to delete → skip it by doing left.next = left.next.next.
        l.next = l.next.next # l -> 2 -> 3 

        return dummy.next # updated head

