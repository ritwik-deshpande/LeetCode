class Solution:
    
    def f(self, A, B):
        if (A, B) in self.dp:
            return self.dp[(A, B)]
        
        if A <= 0 and B <= 0:
            return 0.5
        
        if A <= 0 :
            return 1
        
        if B <= 0:
            return 0
        
        
        c =  (self.f(A - 100, B) + self.f(A - 75, B - 25) + self.f(A - 50, B - 50) + self.f(A - 25, B - 75))*0.25
        
        self.dp[(A, B)] = c
        return c
            
   

    def soupServings(self, n: int) -> float:
        
        if n >= 4300:
            return 1.0
        
        self.dp = {}
        op = self.f(n, n)
        return op
        
        
        
        