"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def f(self, root, d):
        
        if root:
            self.max_d = max(self.max_d, d)
            
            for child in root.children:
                self.f(child, d + 1)
    
    
    def maxDepth(self, root: 'Node') -> int:
        self.max_d = 0
        
        self.f(root, 1)
        
        return self.max_d