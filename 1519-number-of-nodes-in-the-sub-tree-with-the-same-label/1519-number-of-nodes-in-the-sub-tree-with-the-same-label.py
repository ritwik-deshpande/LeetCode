class Solution:
    def f(self, node, visited, labels):
        
        # print(node)
        visited[node] = True
        
        subtree = labels[node]
        for child in self.graph[node]:
            if not visited[child]:
                op = self.f(child, visited, labels)
                subtree = subtree + op
                
                
        cnt = subtree.count(labels[node])
        # print("cnt is", cnt)
        self.ans[node] = cnt
        
        # print(subtree)
        return subtree
            
                
        
            
        
        
    
                
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        self.graph = collections.defaultdict(list)
        visited = [False for _ in range(n)]
        
        for edge in edges:
            self.graph[edge[1]].append(edge[0])
            self.graph[edge[0]].append(edge[1])
            
        self.ans = [1 for _ in range(n)]
        self.f(0, visited, labels)
        
        return self.ans
        
            
        