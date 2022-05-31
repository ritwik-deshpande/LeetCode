# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def insert(self, root, prev, val, pos):
        
        if root:
            if root.val < val:
                self.insert(root.right, root, val, 'r')
                
            else:
                self.insert(root.left, root, val, 'l')
                
        else:
            if pos == 'l':
                node = TreeNode(val)
                prev.left = node
                
            else:
                node = TreeNode(val)
                prev.right = node
                
                
        
        
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return TreeNode(val)
        
        self.insert(root, root, val, '')
        return root