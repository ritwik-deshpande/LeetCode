# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root, max_till_now):
        
        
        if root:
            if root.val >= max_till_now:
                self.count += 1
            max_till_now = max(max_till_now, root.val)
            self.f(root.left, max_till_now)
            self.f(root.right, max_till_now)
            
    
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.f(root, float('-inf'))
        
        return self.count
        