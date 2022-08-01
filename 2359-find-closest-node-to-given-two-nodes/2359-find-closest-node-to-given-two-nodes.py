class Solution:
    
    def dfs(self, node, edges, dist, d):
        
        if dist[node] != float('inf'):
            return dist
        
        dist[node] = d
        
        return self.dfs(edges[node], edges, dist, d + 1)
    
    
    def bfs(self, src, edges, dist):
        
        q = [src]
        dist[src] = 0
        while q:
            root = q.pop(0)
            if edges[root] != -1 and dist[edges[root]] == float('inf'):
                q.append(edges[root])
                dist[edges[root]] = dist[root] + 1
            
    
    # auto bfs=[&](int src, vector<int> &dist,vector<int>& edge,int n){
    #     queue<int> q;
    #     q.push(src);
    #     dist[src]=0;
    #     while(q.size()>0){
    #         auto p= q.front(); q.pop();
    #         if(edge[p]!=-1 and dist[edge[p]]==INT_MAX){
    #            q.push(edge[p]);  
    #            dist[edge[p]]= dist[p]+1;
    #         }
    #     }
    # };
    # int n= e.size();
    # vector<int> A(n,INT_MAX), B(n,INT_MAX);
    # bfs(n1,A,e,n);   bfs(n2,B,e,n);
    # int res= INT_MAX, node=-1;
    # for(int i=0;i<n;i++){
    #     if(A[i]==INT_MAX or B[i]==INT_MAX) continue;
    #     if(res>max(A[i],B[i])) node=i,res= max(A[i],B[i]);
    # }
    # return node;
            
        
    
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        N = len(edges)
        dist1 = [float('inf') for _ in range(N)]
        
        self.bfs(node1, edges, dist1)
        # self.dfs(node1, edges, dist1, 0)
        print(dist1)
        
        dist2 = [float('inf') for _ in range(N)]
        
        self.bfs(node2, edges, dist2)
        # self.dfs(node2, edges, dist2, 0)
        print(dist2)
        
        ans = float('inf')
        d = float('inf')
        
        for i in range(0, N):
            if dist1[i] == float('inf') or dist2[i] == float('inf'):
                continue
                
            if d > max(dist1[i], dist2[i]):
                d = max(dist1[i], dist2[i])
                ans = i
                
            
        if ans == float('inf'):
            return -1
        return ans
        
                
        
        