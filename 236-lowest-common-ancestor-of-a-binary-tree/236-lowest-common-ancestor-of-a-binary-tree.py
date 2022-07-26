# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def f(self, root):
        
        if root:
            if root.val == self.p.val or root.val == self.q.val:
                return root


            l = self.f(root.left)
            r = self.f(root.right)

            if l is not None and r is not None:
                return root

            elif l is not None:
                return l

            else:
                return r
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        
        
        return self.f(root)