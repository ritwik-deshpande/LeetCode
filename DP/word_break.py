class Solution:
    def f(self, s):
        L = len(s)
        print(s, L)
        if s in self.dp:
            return self.dp[s]
        
        if s in self.wordDict:
            return True
        
        
        val = False
        for i in range(1, L):
            sub_s = s[:i]
            new_s = s[i:]
            if sub_s in self.wordDict:
                val = self.f(new_s)
                if val == True:
                    self.dp[s] = True
                    return True
                
        
        self.dp[s] = False  
        return False
            
            
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.dp ={}
        return self.f(s)
        
        
        
        
        