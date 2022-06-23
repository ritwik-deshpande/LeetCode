class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l = 0
        h = int(sqrt(c))
        
        
        while l <= h:
            # print(l, h)
            if l*l + h*h == c:
                return True
            
            elif l*l + h*h > c:
                h -= 1
                
            else:
                l += 1
        
        return False