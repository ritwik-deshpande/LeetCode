# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root):
        
        if root:
            if root.val == self.val:
                self.ans = root
                
            if root.val > self.val:
                self.f(root.left)
                
            elif root.val < self.val:
                self.f(root.right)
        
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.val = val
        self.ans = None
        self.f(root)
        
        return self.ans