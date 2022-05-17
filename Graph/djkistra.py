class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def minDist(self):
        
        min_dist = float('inf')
        min_i = 0
        for i, d in enumerate(self.dist):
            if d < min_dist and not self.found[i]:
                min_dist = d
                min_i = i
                
        return min_i
    
    def dijkstra(self, V, adj, S):
        #code here
        
        self.dist = [float('inf')]*(V)
        self.found = [False]*(V)
        
        self.dist[S] = 0
        
        for _ in range(V):
            x = self.minDist()
            self.found[x] = True
            # print(x)
            for a in adj[x]:
                y = a[0]
                cost = a[1]
                
                if self.dist[y] > self.dist[x] + cost:
                    self.dist[y] = self.dist[x] + cost
                # print(self.dist)
        return self.dist