class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        # print(adj)
        ans = []
        
        queue = []
        queue.append(0)
        visited = [False]*len(adj)
        
        while len(queue) != 0:
            v = queue.pop(0)
            ans.append(v)
            for adj_v in adj[v]:
                if not visited[adj_v]:
                    queue.append(adj_v)
                    visited[adj_v] = True
        return ans