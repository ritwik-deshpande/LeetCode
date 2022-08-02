class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        grp = [1]
        idx = 0
        i = 1
        L = len(s)
        while i < L:
            
            if s[i - 1] != s[i]:
                idx += 1
                grp.append(1)
                
                
            else:
                grp[idx] += 1
                
            i += 1
            
        
        print(grp)
        
        ans = 0
        i = 1
        L = len(grp)
        while i < L:
            
            ans += min(grp[i], grp[i - 1])
            
            i += 1
            
        
        return ans
                
            
            

            