class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        l = math.lcm(p, q)
        
        if (l//q)%2 == 0:
            return 2
        
        return (l//p)%2
        