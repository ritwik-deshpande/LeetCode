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
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.ans = []
        
        self.f(root)
        
        l = 0
        r = len(self.ans) - 1
        
        while l < r:
            if self.ans[l] + self.ans[r] == k:
                return True
            elif self.ans[l] + self.ans[r] > k:
                r -= 1
                
            else:
                l += 1
                
        return False
        