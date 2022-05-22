# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def f(self, root, root2):
        if root is None:
            return root2
        
        if root:
            root2 = self.f(root.left, root2)
            root2.val = root.val
            root2.left = None
            root2.right = TreeNode(-1)
            root2 = root2.right
            root2 = self.f(root.right, root2)
            
            return root2
            
        
        
    
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        root2 = TreeNode()
        
        self.f(root, root2)
        tmp = root2
        while tmp.val != -1:
            prev = tmp
            tmp = tmp.right

        prev.left = None
        prev.right = None
        return root2