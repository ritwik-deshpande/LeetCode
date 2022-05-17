class Solution:
    def f(self, pos1, pos2):
        if (pos1, pos2) in self.dp:
            return self.dp[(pos1, pos2)]
        
        if pos1 >= self.L1 or pos2 >= self.L2:
            return 0
        
        if self.text1[pos1] == self.text2[pos2]:
            retval = self.f(pos1 + 1, pos2 + 1) + 1
            
        else:
            retval_1 = self.f(pos1, pos2 + 1)
            retval_2 = self.f(pos1 + 1, pos2)
            retval = max(retval_1, retval_2)
        
        self.dp[(pos1, pos2)] = retval
        return retval
        
        
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.L1 = len(text1)
        self.L2 = len(text2)
        self.text1 = text1
        self.text2 = text2
        self.dp = {}
        return self.f(0, 0)
        
        
        