class Solution:
    
    
    def f(self, m, n):
        
        if (m, n) in self.dp:
            return self.dp[(m, n)]
        
        if m == -1 :
            return n + 1
        
        if n == -1:
            return m + 1
        
        if self.word1[m] == self.word2[n]:
            retval = self.f(m-1, n-1)
        else: 
            op_1 = self.f(m-1, n)
            op_2 = self.f(m, n-1)
            op_3 = self.f(m-1, n-1)
            retval = min(op_1, op_2, op_3) + 1
            
        self.dp[(m, n)] = retval
        return self.dp[(m, n)]
        
        
    
    
    def minDistance(self, word1: str, word2: str) -> int:
        
        self.word1 = word1
        self.word2 = word2
        self.dp = {}
        
        m = len(word1)
        n = len(word2)
        
        return self.f(m-1, n-1)
        
        
        