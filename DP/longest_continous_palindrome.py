class Solution:
    
        
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        L = len(s)
        self.dp = [[False]*len(s) for _ in range(len(s))]
        
        max_len = 0
        
        for i in range(L):
            self.dp[i][i] = True
            max_len = 1
            max_i = i
            
            
        for i in range(L - 1):
            if s[i] == s[i+1]:
                self.dp[i][i+1] = True
                max_len = 2
                max_i = i
                
        # print(max_len, i)
            
        for pal_len in range(2, L):
            for i in range(L - pal_len):
                if s[i] == s[i + pal_len] and self.dp[i+1][i + pal_len - 1]:
                    self.dp[i][i + pal_len] = True
                    # print(max_len, pal_len)
                    if max_len < pal_len + 1:
                        # print(max_len, pal_len)
                        max_len = pal_len + 1
                        max_i = i
                    
                    
                    
        # print(max_len, i)
                    
        return s[max_i: max_i + max_len]
                
                