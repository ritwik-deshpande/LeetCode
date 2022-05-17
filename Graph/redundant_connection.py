from collections import defaultdict
class Solution:
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        self.parent = defaultdict(int)
        
        for edge in edges:
            
            v, u = edge[0], edge[1]
            if u not in self.parent:
                self.parent[u] = u
                
            if v not in self.parent:
                self.parent[v] = v
            
            x = self.find(v)
            y = self.find(u)
            
            if x!=y:
                self.parent[y] = x
            
            else:
                return edge
            
        