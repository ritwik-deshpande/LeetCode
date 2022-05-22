# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, parent, d):
        
        if root:
            if root.val == self.x:
                self.d1 = d
                self.parent1 = parent
                
            if root.val == self.y:
                self.d2 = d
                self.parent2 = parent
                
            self.f(root.left, root.val, d + 1)
            self.f(root.right, root.val, d + 1)
            
                
            
            
    
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x = x
        self.y = y

        
        self.f(root, -1, 0)
        
        if self.d1 == self.d2 and self.parent1 != self.parent2:
            return True
        
        return False
        
        