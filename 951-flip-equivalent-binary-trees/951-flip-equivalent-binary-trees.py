# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root1, root2):
        
        if root1 is None and root2 is None:
            return True
        
        if root1 and root2:
            if root1.val == root2.val:
                op1 = self.f(root1.left, root2.left)
                op2 = self.f(root1.right, root2.right)
                
                
                op3 = self.f(root1.left, root2.right)
                op4 = self.f(root1.right, root2.left)
                
                return ((op1 & op2) | (op3 & op4))
            
        return False
    
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.f(root1, root2)