class Solution:
    
    def f(self, m, n):
        if (m, n) in self.dp:
            return self.dp[(m, n)]
        
        if m < 0 or n < 0 or m >= self.M or n >= self.N:
            return 0
        
        if m == self.M - 1 and n == self.N - 1:
            return 1
        
        retval =  self.f(m + 1, n) + self.f(m, n + 1)
        self.dp[(m, n)] = retval
        return retval
        
        
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        self.M = m
        self.N = n
        
        self.dp = {}
        
        return self.f(0, 0)
        