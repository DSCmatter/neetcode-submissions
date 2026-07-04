class Solution:
    def copyRandomList(self, head: 'Optional[Node]', memo={}) -> 'Optional[Node]':
        if not head:
            return None 
        
        if head in memo:
            return memo[head]

        newNode = Node(head.val)
        memo[head] = newNode
        newNode.next = self.copyRandomList(head.next, memo)
        newNode.random = self.copyRandomList(head.random, memo)
        return newNode