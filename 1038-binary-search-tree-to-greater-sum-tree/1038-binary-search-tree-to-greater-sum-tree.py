# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, val):
        
        if root is None:
            return 0
        
        if root:
            
            v2 = self.f(root.right, val)
            tmp = root.val
            root.val = root.val + v2 + val
            
            v1 = self.f(root.left, root.val)
            
            return v1 + v2 + tmp
            
            
            
    
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.f(root, 0)
        
        return root
        
        