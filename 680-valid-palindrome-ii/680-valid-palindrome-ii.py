class Solution:
    def check(self, l, h, s, count):
        
        if l >= h:
            return True
        
        
        if s[l] != s[h]:
            if count > 0:
                return False
            
            else:
                return self.check(l + 1, h, s, count + 1) | self.check(l, h - 1, s, count + 1)
            
        else:
            return self.check(l + 1, h - 1, s, count)
        
        
    
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        h = len(s) - 1
        
        return self.check(l, h, s, 0)
                
            
        