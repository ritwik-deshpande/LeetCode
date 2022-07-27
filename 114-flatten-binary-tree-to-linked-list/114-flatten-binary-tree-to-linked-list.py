# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def f(self, root):
        
       
        
        if root:
            if root.left is None and root.right is None:
                return root
            
            l = self.f(root.left)
            r = self.f(root.right)
            
            # print(l, r)
            
            if l is not None:
                tmp = l
                while tmp.right is not None:
                    tmp = tmp.right
                tmp.right = r
                root.right = l
            else:
                root.right = r   
            root.left = None
            return root
        
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.f(root)