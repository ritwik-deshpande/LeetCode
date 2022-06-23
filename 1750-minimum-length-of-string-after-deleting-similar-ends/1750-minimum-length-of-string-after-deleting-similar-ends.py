class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        h = len(s) - 1
        cc = ''
        while l < h:
            
            if s[l] == s[h]:
                cc = s[l]
                
                
                while l < h and s[l] == cc:
                    l += 1
                    
                    
                while l < h and s[h] == cc:
                    h -= 1
            else:
                break
                    
        # print(l, h) 
        if l == h and cc == s[l]:
            return 0
        
        return h - l + 1
                
                
                