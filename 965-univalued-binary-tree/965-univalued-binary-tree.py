# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self, root):
        
        if root:
            # print(self.val, root.val)
            if self.val != -1 and self.val != root.val:
                return False
            
            self.val = root.val
            return self.check(root.left) & self.check(root.right)
        else:
            return True
    
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.val = -1
        
        return self.check(root)