from collections import defaultdict

class Solution:
        
    
    def findOrder(self, numCourses, prerequisites):
        
        self.graph = defaultdict(list)
        self.indegree = defaultdict(int)
        for i in range(numCourses):
            self.indegree[i] = 0
        self.queue = []
        res = []
        
        for edge in prerequisites:
            self.graph[edge[1]].append(edge[0])
            self.indegree[edge[0]] += 1
            
            
            
        for v in self.indegree:
            if self.indegree[v] == 0:
                self.queue.append(v)
                
        print(self.indegree)
            
        while len(self.queue) != 0:
            x = self.queue.pop(0)
            res.append(x)
            for v in self.graph[x]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    self.queue.append(v)
        
        if len(res) != numCourses:
            return []
         
        return res