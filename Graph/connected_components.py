class Solution:
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])
        
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        self.parent = [i for i in range(0, n)]
        
        for v in range(0, n):
            for u in range(0, n):
                if isConnected[v][u] == 1:
                    x = self.find(v)
                    y = self.find(u)
                    print(v,u, x, y)
                    if x != y:
                        self.parent[y] = x
                    
                    
        
        for index, val in enumerate(self.parent):
            self.parent[index] = self.find(val)
            
        print(self.parent)  
        return len(set(self.parent))
        
        
if __name__ =='__main__':
    Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])

            
        