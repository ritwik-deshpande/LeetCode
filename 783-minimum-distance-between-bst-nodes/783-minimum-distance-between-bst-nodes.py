# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def f(self, root, path):
        
        if root:
            self.diff = min(min([abs(root.val - val) for val in path]), self.diff)    
            path = path + [root.val]
            self.f(root.left, path)
            self.f(root.right, path)
            
    
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.diff = float('inf')
        
        self.f(root, [float('inf')])
        
        return self.diff