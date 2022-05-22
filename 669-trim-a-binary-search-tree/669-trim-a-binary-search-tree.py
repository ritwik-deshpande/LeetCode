# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
        
    
    def f(self, root, parent):
        
        if root:
            if root.val < self.low:
                if parent is None:
                    self.root = root.right
                else:
                    parent.left = root.right
                self.f(root.right, parent)
                
            elif root.val > self.high:
                if parent is None:
                    self.root = root.left
                else:
                    parent.right = root.left
                
                self.f(root.left, parent)
                
            else:
                self.f(root.left, root)
                self.f(root.right, root)
    
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.low = low
        self.high = high
        self.root = root
        self.f(root, None)
        
        # self.inorder(root)
        return self.root