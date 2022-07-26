# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def f(self, root, path):
        
        if root:
            path = path + [root]
            if root.val == self.p.val:
                self.p_path = path
                
            if root.val == self.q.val:
                self.q_path = path
                
            
            self.f(root.left, path)
            self.f(root.right, path)
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.f(root, [])
        
        i = 0
        # print(self.p_path, self.q_path)
        
        while i < min(len(self.p_path), len(self.q_path)) and self.p_path[i].val == self.q_path[i].val :
            i = i + 1
            
        return self.p_path[i - 1]
        