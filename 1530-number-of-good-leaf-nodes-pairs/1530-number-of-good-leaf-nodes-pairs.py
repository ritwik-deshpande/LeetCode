# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPairs(self, d1, d2):
        
        for d_i in d1:
            for d_j in d2:
                if abs(d_i + d_j) <= self.d:
                    self.ans += 1
    
    def f(self, root):
        
        
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [0]
        
        if root:
            d_l = [p + 1 for p in self.f(root.left)]
            
            d_r = [p + 1 for p in self.f(root.right)]
            
            self.findPairs(d_l, d_r)
            # print(d_l, d_r, root.val)
            return d_l + d_r
            
             
    
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.d = distance
        self.ans = 0
        
        self.f(root)
        
        return self.ans
        