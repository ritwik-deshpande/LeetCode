class Solution:
    
    def isConnected(self, b1, b2):
        
        x1 = b1[0]
        y1 = b1[1]
        x2 = b2[0]
        y2 = b2[1]
        
        r1, r2 = b1[2], b2[2]
        
        d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        if d <= r1:
            return True
        
        return False
            
        
    def bfs(self, i, graph):
        visited = []
        
        q = [i]
        cnt = 0
        # print('start')
        while q:
            b = q.pop(0)
            
            if b not in visited:
                visited.append(b)
                
                for child in graph[b]:
                    q.append(child)
                
                cnt += 1
                
        return cnt

            
        
        
        
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
       
        graph = collections.defaultdict(list)
        
        L = len(bombs)
        
        
        
        for i in range(L):
            for j in range(L):
                if self.isConnected(bombs[i], bombs[j]) and i != j:
                    graph[i].append(j)
                    
                
            
        # print(self.graph)
        
        
        ans = 1
        for i in range(len(bombs)):
            ans = max(ans, self.bfs(i, graph))
            
        
        return ans