# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in the inorder array for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track our current position in the preorder array
        self.pre_idx = 0
        
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # Base case: if there are no elements to construct the subtree
            if left > right:
                return None
            
            # Select the root value from preorder and increment the pointer
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Get the split point index in the inorder array
            mid = inorder_map[root_val]
            
            # Recursively build the left and right subtrees
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)


