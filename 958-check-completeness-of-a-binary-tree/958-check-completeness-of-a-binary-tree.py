# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
            
    
    def check(self, root):
        
        q = [root]
        prev = root
        
        while len(q) != 0:
            
            root = q.pop(0)
            
            if root:
                if prev is None:
                    return False
                q.append(root.left)
                q.append(root.right)
                
            prev = root
                
        return True
            
            
            
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        return self.check(root)