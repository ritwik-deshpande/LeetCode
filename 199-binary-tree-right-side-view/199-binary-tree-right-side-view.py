# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, n):
        
        ans = collections.defaultdict(list)
        
        q = [(n, 0)]
        
        while len(q) != 0:
            
            root, level = q.pop(0)
            
            if root:
                ans[level].append(root.val)
                
                q.append((root.left, level + 1))
                q.append((root.right, level + 1))
                
        return ans.values()
            
            
        
    
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        levels = self.f(root)
        
        for level in levels:
            ans.append(level[-1])
        
        return ans