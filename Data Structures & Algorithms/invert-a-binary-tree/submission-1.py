# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # using bfs to swap left and right children 
        if not root: 
            return None 
        
        queue = deque([root]) # initialize queue and insert the root node 

        while queue:
            # remove the front node
            node = queue.popleft()
            # perform swap
            node.right, node.left = node.left, node.right 

            # if left & right child are not empty then append 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root 
