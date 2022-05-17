class Solution:
    
    def f(self, m, n):
        
        if (m, n) in self.dp:
            return self.dp[(m, n)]
        
        if (n == 0 and self.grid[m][n] == -1) or (n == self.N - 1 and self.grid[m][n] == 1) or \
            (n < self.N -1 and self.grid[m][n] == 1 and self.grid[m][n+1] == -1) or \
            (n > 0 and self.grid[m][n - 1] == 1 and self.grid[m][n] == -1):
            return -1
        
        
        if m == self.M - 1:
            if self.grid[m][n] == 1:
                return n + 1
            else:
                return n - 1
            
        
        if self.grid[m][n] == 1:
            retval = self.f(m + 1, n + 1)   
        else: 
            retval = self.f(m + 1, n - 1)
            
        self.dp[(m, n)] = retval
        return retval
        
        
    
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])
        
        self.dp = {}
        ans = []
        
        for i in range(self.N):
            op = self.f(0, i)
            ans.append(op)
        
        return ans
            
            
            
            