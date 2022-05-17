# cook your dish here
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def util(self, root, targetSum):
        if root:
            self.f(root, targetSum)
            self.util(root.left, targetSum)
            self.util(root.right, targetSum)
        
        
    def f(self, root, t):
        
        
        if root:
            t -= root.val
            if t == 0:
                # print("The t is ", t, self.ans)
                self.ans = self.ans + 1
            
            # print("the root", root.val, t)
            self.f(root.left, t)
            self.f(root.right, t)
        
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.util(root, targetSum)
        return self.ans
        
        