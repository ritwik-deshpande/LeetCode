class Solution:
    
    def f(self, i, j):
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        if i == self.M or j == self.N or self.m[i][j] == '0':
            return 0
        
        
        self.dp[(i, j)] = 1 + min(self.f(i + 1, j), self.f(i, j + 1), self.f(i + 1, j + 1))
        return self.dp[(i, j)]
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        self.M = len(matrix)
        self.N = len(matrix[0])
        self.m = matrix
        self.dp = {}
        
        ans = 0
        for i in range(self.M):
            for j in range(self.N):
                
                ans = max(ans, self.f(i, j))
        
        
        return ans*ans