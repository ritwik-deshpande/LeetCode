"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        q = [(root, 0)]
        
        levels = collections.defaultdict(list)

        while len(q) != 0:
            
            root, l = q.pop(0)
            
            if root:
                levels[l].append(root.val)

                for child in root.children:
                    q.append((child, l + 1))
                
    
        return levels.values()
            
            