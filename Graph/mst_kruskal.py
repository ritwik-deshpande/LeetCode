class Solution:
    
    def find(self, x):
        
        if x == self.parent[x]:
            return x
        
        return self.find(self.parent[x])
        
    def union(self, x, y):
        
        self.parent[x] = y
        
        
    
    
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        
        self.parent = [ i for i in range(len(points))]
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
                edges.append([i, j, dist])
                
                
        edges = sorted(edges, key = lambda x : x[2])
        
        # print(edges)
        
        e = 0
        ans = 0
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            
            x = self.find(u)
            y = self.find(v)
            
            if x != y:
                self.union(x, y)
                e = e + 1
                ans = ans + edge[2]
                
            if e == len(points) - 1:
                return ans
            
                    
        
        return 0