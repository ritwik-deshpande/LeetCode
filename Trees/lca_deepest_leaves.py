# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root):
        if root is None:
            return None, 0
        
        
        lca_l, l_d = self.f(root.left)
        lca_r, r_d = self.f(root.right)
        
        if l_d == r_d:
            return root, l_d + 1
        elif l_d > r_d:
            return lca_l, l_d + 1
        else:
            return lca_r, r_d + 1
        
        
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.f(root)[0]