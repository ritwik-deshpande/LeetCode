class Solution:
    
    def ascii_value(self, s):
        ans = 0
        for ch in s:
            ans = ans + ord(ch)
            
        return ans
        
    
    def f(self, pos1, pos2):
        
        if (pos1, pos2) in self.dp:
            return self.dp[(pos1, pos2)]
        
        if pos1 == self.m:
            return self.ascii_value(self.s2[pos2:])
        
        if pos2 == self.n:
            return self.ascii_value(self.s1[pos1:])
        
        if self.s1[pos1] == self.s2[pos2]:
            retval = self.f(pos1 + 1, pos2 + 1)
            
        else:
            op1 = self.f(pos1 + 1, pos2) + self.ascii_value(self.s1[pos1])
            op2 = self.f(pos1, pos2 + 1) + self.ascii_value(self.s2[pos2])
            retval = min(op1, op2)
            
        self.dp[(pos1, pos2)] = retval
            
        return retval
            
        
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        self.s1 = s1
        self.s2 = s2
        self.m = len(s1)
        self.n = len(s2)
        self.dp = {}
        
        return self.f(0, 0)
        