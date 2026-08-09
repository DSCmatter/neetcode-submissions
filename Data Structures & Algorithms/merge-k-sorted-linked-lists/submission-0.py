# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # given already sorted linked lists 
        # return merged sub arrays into one sorted array 

        nodes = []

        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        res = ListNode(0) # dummy head 
        curr = res 
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next 
        return res.next