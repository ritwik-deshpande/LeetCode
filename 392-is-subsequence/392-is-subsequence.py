class Solution(object):
   
    
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        L = len(s)
        while i < L:
            if j == len(t):
                break
            
            if s[i] == t[j]:
                i += 1
                j += 1
                    
            else:
                j += 1
                
           
        if i != L:
            return False
            
        return True