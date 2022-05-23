# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root):
        
        if root:
            self.f(root.left)
            self.ans.append(root.val)
            self.f(root.right)
    
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = []
        
        self.f(root)
        for i in range(1, len(self.ans)):
            if self.ans[i - 1] >= self.ans[i]:
                return False
            
        return True
        
        