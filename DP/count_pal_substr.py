# cook your dish here
class Solution:
    
        
        
        
        
    def countSubstrings(self, s: str) -> int:
        L = len(s)
        self.dp = [[False]*len(s) for _ in range(len(s))]
        
        count = 0 
        
        for i in range(L):
            self.dp[i][i] = True
            count = count + 1
           
            
        for i in range(L - 1):
            if s[i] == s[i+1]:
                self.dp[i][i+1] = True
                count = count + 1
                
        # print(max_len, i)
            
        for pal_len in range(2, L):
            for i in range(L - pal_len):
                if s[i] == s[i + pal_len] and self.dp[i+1][i + pal_len - 1]:
                    self.dp[i][i + pal_len] = True
                    count = count + 1
                    
                    
                    
        # print(max_len, i)
                    
        return count
                
