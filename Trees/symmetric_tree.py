# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, left_node, right_node):
        
        if left_node and right_node and left_node.val == right_node.val:
            
            return self.check(left_node.left, right_node.right) & self.check(left_node.right, right_node.left)
        
        elif left_node is None and right_node is None:
            return True
    
        return False
    
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.check(root.left, root.right)