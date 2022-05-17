class Solution:
    def findJudge(self, n, trust):
        
        self.graph = defaultdict(set)
        
        for edge in trust:
            self.graph[edge[0]].add(edge[1])
            
        
        
        judge = set([ i for i in range(1, n+1)]) 
        
        for v in range(1, n+1):
            self.graph[v].add(v)
            
        print(self.graph)
            
        for v in range(1, n+1):
            print(judge, self.graph[v])
            judge = judge & self.graph[v]
            
        judge = list(judge)
        print(judge)
        if len(judge) != 1:
            return -1
        
        elif len(self.graph[judge[0]]) != 1:
            return -1
        return judge[0]
        
        
if __name__ =='__main__':
    Solution().findJudge(3, [[1,3],[2,3],[3,1]])
    Solution().findJudge(3, [[1,3],[2,3]])
    
            
        