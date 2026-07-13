# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1st phase
        # take 2nd portion of list and reverse it: 3->4 becomes 3<-4 
        # take both portions 1st and 2nd and merge them together
        # how do we know if we are in 2nd portion? we use fast and slow pointers 
        # slow ptr goes 1x but fast goes twice as fast - 2x 
        # point slow at head and fast at head.next 
        # iterating over we get slow at head.next and fast at head.next.next
        # we shift fast ptr by 2 so make a temp node '5'

        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        # beginning of 2nd half of list
        second = slow.next
        prev = slow.next = None 

        while second:
            tmp = second.next
            second.next = prev 
            prev = second # update ptr
            second = tmp 

        # merge two halfs of the list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1 
            first, second = tmp1, tmp2  