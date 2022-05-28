# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, preorder):
        
        if len(preorder) > 0:
            root = TreeNode(0)
            root_val = preorder[0]
            root.val = root_val
            
            i = 1
            L = len(preorder)
            while i < L and preorder[i] < root_val:
                i += 1
                
                
            left_preorder = preorder[1 : i]
            right_preorder = preorder[i : ]
            
            root.left = self.construct(left_preorder)
            root.right = self.construct(right_preorder)
            
            return root
        
        else:
            return None
            
            
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        return self.construct(preorder)