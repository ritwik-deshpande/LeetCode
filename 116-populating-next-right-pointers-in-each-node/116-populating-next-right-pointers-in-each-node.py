"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def f(self, root):
        
        q = [(root, 0)]
        p = (None, - 1)
        while q:
            r, l = q.pop(0)
        
            
            if p[0] and p[1] == l:
                p[0].next = r
            # print(r.val, l, p[0].val)
            p = (r, l)
            if r:
                # print(r.val)
                q.append((r.left, l + 1))
                q.append((r.right, l + 1))
            
        return root
    
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        
        return self.f(root)