# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, root):
        
        if root:
            self.f(root.left)
            self.ans.append(root.val)
            self.f(root.right)
    
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        self.ans = []
        self.f(root1)
        self.f(root2)
        
        return sorted(self.ans)