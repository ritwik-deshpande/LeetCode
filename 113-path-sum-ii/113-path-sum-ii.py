# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def f(self, root, path, t):
        
        if root:
            if root.left is None and root.right is None and t - root.val == 0:
                path += [root.val]
                self.ans.append(path)
                
            self.f(root.left, path + [root.val], t - root.val)
            self.f(root.right, path + [root.val], t - root.val)
            
    
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.ans = []
        self.f(root, [], targetSum)
        
        return self.ans