# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getPath(self, root, path):
        if root:
            if root.val == self.target.val:
                self.path = path + [root.val]
                
            self.getPath(root.left , path + [root.val])
            self.getPath(root.right, path + [root.val])
                
            
    def f(self, root, d):
        
        if root:
            if root.val in self.path:
                d = d - 1
            
            else:
                d = d + 1
                
            # print(d, root.val)
            if self.k == d:
                self.ans.append(root.val)
                
            self.f(root.left, d)
            self.f(root.right, d)
            
            
            
            
        
    
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.path = []
        self.target = target
        self.k = k
        
        self.getPath(root, [])
        
        
        print(self.path)
        
        self.ans = []
        self.f(root, len(self.path))
        
        return self.ans