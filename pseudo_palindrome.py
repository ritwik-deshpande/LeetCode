# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, path_dict):
        num_odd_items = 0
        
        for val in path_dict.values():
            if val%2 == 1:
                num_odd_items += 1
                
            if num_odd_items > 1:
                return False
            
        return True
        
        
    
    def f(self, root):
        
        if root and root.left is None and root.right is None:
            self.path[root.val] += 1
            if self.isValid(self.path):
                self.ans += 1
            self.path[root.val] -= 1
                
        if root:
            self.path[root.val] += 1
            self.f(root.left)
            self.f(root.right)
            self.path[root.val] -= 1
            
            
            
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.path = collections.defaultdict(int)
        self.f(root)
        return self.ans
        
        
        
        
        
        
        
        