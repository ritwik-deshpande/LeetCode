# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def construct(self, preorder, inorder):
        
        
        if len(preorder) > 0 and len(inorder) > 0:
            root = TreeNode(0)
            root_val = preorder[0]
            root.val = root_val
            
            # print(preorder, inorder)
            
            
            root_idx = inorder.index(root_val)
            
            
            left_inorder = inorder[:root_idx]
            right_inorder = inorder[root_idx + 1:]
            
            l_i = len(left_inorder) + 1
                
            left_preorder = preorder[1: l_i]
            right_preorder = preorder[l_i:]
            
            root.left = self.construct(left_preorder, left_inorder)
            root.right = self.construct(right_preorder, right_inorder)
            
            return root
        
        else:
            return None
            
            
            
            
            
        
    
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        return self.construct(preorder, inorder)
        
        