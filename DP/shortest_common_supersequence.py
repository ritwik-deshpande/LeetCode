class Solution:
    def f(self, pos1, pos2, str1, str2, L1, L2, dp):
        # print(pos1, pos2)
        
        
        if pos1 == L1:
            diff = L2 - pos2
            return diff, str2[pos2:]
        
        if pos2 == L2:
            diff = L1 - pos1
            return diff, str1[pos1:]
        
        if dp[pos1][pos2] != -1:
            return dp[pos1][pos2]
        
        if str1[pos1] == str2[pos2]:
            
            retval, lcs = self.f(pos1 + 1, pos2 + 1, str1, str2, L1, L2, dp)
            retval = retval + 1
            lcs =  str1[pos1] + lcs
            # print('lcs', lcs)
            
        else:
            retval_1, lcs_1 = self.f(pos1, pos2 + 1, str1, str2, L1, L2, dp)
            # print('lcs_1', lcs_1)
            retval_2, lcs_2 = self.f(pos1 + 1, pos2, str1, str2, L1, L2, dp)
            # print('lcs_2', lcs_2)
            retval = min(retval_1, retval_2)
            if retval == retval_1:
                retval = retval + 1
                lcs =  str2[pos2] + lcs_1 
            else:
                retval = retval + 1
                lcs =  str1[pos1] + lcs_2 
            
        # print(retval, lcs)
        dp[pos1][pos2] = retval, lcs
        return retval, lcs
    
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        
        L1 = len(str1)
        L2 = len(str2)
        dp = [[-1]*L2 for _ in range(L1)]
        
        l, lcs = self.f(0, 0, str1, str2, L1, L2, dp)
        # print("LCS", lcs)
        return lcs
        