class Solution:
    def bellman_ford(self, n, edges):
    #Code here
    dist = [float('inf')]*n
    dist[0] = 0
    for _ in range(n-1):
        for edge in edges:
            a = edge[0]
            b = edge[1]
            c = edge[2]
        
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
    print(dist)
    
if __name__ =='__main__':
    
    
    
    Solution().dijkstra(3, [[0,1,5],[0,2,6],[2,1,-3]])