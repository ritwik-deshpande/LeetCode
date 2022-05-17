from collections import defaultdict

class Solution:
    def topo(self, v):
        
        self.visited[v] = True
        
        for adj in self.graph[v]:
            if not self.visited[adj]:
                self.topo(adj)
        
        self.stack.append(v)
        
    
    def findOrder(self, numCourses, prerequisites):
        
        self.graph = defaultdict(list)
        
        self.visited = [ False for i in range(numCourses)]
        
        start_vertex = [ i for i in range(numCourses)]
        
        self.stack = []
        
        for edge in prerequisites:
            self.graph[edge[1]].append(edge[0])
            if edge[0] in start_vertex:
                start_vertex.remove(edge[0])
            
            
        if len(start_vertex) == 0:
            return []
            
        for v in start_vertex:
            self.topo(v)   
            
        print(self.stack[::-1])
        positions = {}
        
        for i, ele in enumerate(self.stack[::-1]):
            positions[ele] = i
            
        if len(positions.keys()) != numCourses:
            return []
            
        for i in range(numCourses):
            for adj in self.graph[i]:
                child = positions[adj]
                parent = positions[i]
                
                if child < parent:
                    return []
        
        return self.stack[::-1]
        
        
        
        
        
if __name__ =='__main__':
    print(Solution().findOrder(4, [[1,0],[2,1],[3,2],[1,3]]))
    print(Solution().findOrder(2, [[1,0],[0,1]]))
    print(Solution().findOrder(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]))