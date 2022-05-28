# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, preorder, postorder):
        
        
        if len(preorder) > 0 and len(postorder) > 0:
            
            root = TreeNode(0)
            root_val = preorder[0]
            root.val = root_val
            
            # print(preorder, postorder)
            if len(preorder) > 1:
                left_root_val = preorder[1]
                
                idx = postorder.index(left_root_val)
                
                left_postorder = postorder[:idx+1]
                right_postorder = postorder[idx+1 : -1]
                
                l_i = len(left_postorder) + 1
                
                left_preorder = preorder[1: l_i]
                right_preorder = preorder[l_i :]
                
                root.left = self.construct(left_preorder, left_postorder)
                root.right = self.construct(right_preorder, right_postorder)
                
            else:
                root.left = None
                root.right = None
                
            return root
        
        else:
            return None
        
        
    
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.construct(preorder, postorder)