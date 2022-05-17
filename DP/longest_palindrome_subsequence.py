class Solution:
    
    def f(self, start, end):
        
        # print(start, end)
        if (start, end) in self.dp:
            return self.dp[(start, end)]
        
        if start == end:
            return 1
        
        if start > end:
            return 0
        
        
        if self.s[start] == self.s[end]:
            retval = self.f(start + 1, end -1) + 2
        else:
            retval_2 = self.f(start + 1, end) 
            retval_3 = self.f(start, end - 1)
            retval = max(retval_2, retval_3)
            
        # print(retval)
        self.dp[(start, end)] = retval
    
        return retval
        
        
        
    
    def longestPalindromeSubseq(self, s: str) -> int:
        self.s = s
        
        self.dp = {}
        return self.f(0, len(s) - 1)
        
        