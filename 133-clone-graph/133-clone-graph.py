"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def f(self, node2):
        
        if node2:
        
        # print(node2.val)
            if node2.val in self.map:
                return self.map[node2.val]
            else:
                new_node = Node(node2.val)
                self.map[new_node.val] = new_node
                for child in node2.neighbors:

                    new_child = self.f(child)
                    new_node.neighbors.append(new_child)



                return new_node
            
        
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        self.map = collections.defaultdict(Node)
        
        return self.f(node)
        
        
        