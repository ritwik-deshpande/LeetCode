from collections import defaultdict

class Solution:
    def minDist(self):
        
        min_d = float('inf')
        min_i = 0
        
        for i, d in enumerate(self.dist):
            if d < min_d and not self.found[i]:
                min_d = d
                min_i = i
                
        return min_i
        
    def networkDelayTime(self, times, n: int, k: int) -> int:
        
        self.found = [False]*n
        self.dist = [float('inf')]*n
        
        self.graph = defaultdict(list)
        
        for time in times:
            self.graph[time[0] - 1].append([time[1] -1, time[2]])
            
        self.dist[k-1] = 0
        
        for _ in range(n):
            x = self.minDist()
            self.found[x] = True
            # print(x)
            for a in self.graph[x]:
                y = a[0]
                cost = a[1]
                if self.dist[y] > self.dist[x] + cost:
                    self.dist[y] = self.dist[x] + cost
                    
        ans = max(self.dist)
        
        if ans == float('inf'):
            return -1
        return ans
                    