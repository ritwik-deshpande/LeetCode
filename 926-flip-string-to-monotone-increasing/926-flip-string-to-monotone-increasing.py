class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        one = 0
        flip = 0
        for ch in s:
            
            if ch == '1':
                one += 1
                
            elif ch == '0' and one >= 1:
                flip = min(flip + 1, one)
                
        return flip
                
                
            