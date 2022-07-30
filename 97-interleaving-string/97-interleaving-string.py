class Solution:
    
    def f(self, i, j, k):
        
        if (i,j,k) in self.dp:
            return self.dp[(i,j,k)]
        
        if i == len(self.s1) and j == len(self.s2) and k == len(self.s3):
            return True
        
        r1 = False
        r2 = False
        
        if i < len(self.s1) and k < len(self.s3) and self.s1[i] == self.s3[k] :
            r1 = self.f(i + 1, j, k + 1)
            
        if j < len(self.s2) and k < len(self.s3) and self.s2[j] == self.s3[k] :
            r2 = self.f(i, j + 1, k + 1)
            
        
        
        self.dp[(i,j,k)] =  r1 | r2
        return r1 | r2
        
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        
        self.dp = {}
        return self.f(0, 0, 0)
        
        