from collections import defaultdict

class Solution:
    def bfs(self, src):
        
        queue = [(src, 1)]
        self.color[src] = 1
        
        while len(queue) != 0:
            root, color = queue.pop(0)
            
            if self.visited[root]:
                continue
                
            self.visited[root] = True
                
            for ngb in self.graph[root]:
                
                if ngb in self.color and self.color[ngb] == color:
                    return False
                
                else:
                    queue.append((ngb, (-1)*color))
                    self.color[ngb] = (-1)*color
                
                
        return True
            
            
            
            
    
    def possibleBipartition(self, n, dislikes):
        
        
        self.graph = defaultdict(list)
        
        for edge in dislikes:
            self.graph[edge[0]].append(edge[1])
            # self.graph[edge[1]].append(edge[0])
        
        self.visited = [False]*(n + 1)
        self.color = {}
        
        
        
        for v in range(1, n+1):
            
            if not self.visited[v]:
                
                retval = self.bfs(v)
                print(self.color, self.visited)
                if retval == False:
                    return False
                
        return True
        
        
        
if __name__ =='__main__':
    print(Solution().possibleBipartition(6, [[1,2],[2,6],[3,4],[4,5],[5,6]]))
    