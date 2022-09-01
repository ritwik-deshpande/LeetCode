class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        self.graph = collections.defaultdict(list)
        self.iedges = collections.defaultdict(int)
        
        
        for pre in prerequisites:
            self.graph[pre[1]].append(pre[0])
            self.iedges[pre[0]] += 1
            
        courses = []    
        q = []
        
        for c in range(numCourses):
            if self.iedges[c] == 0:
                q.append(c)
                
        # print(q)
        while q:
            root = q.pop()
            courses.append(root)
            
            for child in self.graph[root]:
                self.iedges[child] -= 1
                if self.iedges[child] == 0:
                    q.append(child)

        if len(courses) == numCourses:
            return True
        
        return False