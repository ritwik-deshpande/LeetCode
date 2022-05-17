class Solution:
    def f(self, x, y, n):
        if (x, y, n) in self.dp:
            return self.dp[(x, y, n)] 
        
        if x > 3 or y > 2 or x < 0 or y < 0 or (x == 3 and y == 0) or (x == 3 and y == 2):
            return 0
        
        if n == 1:
            return 1
        
        retval =    self.f(x + 2, y - 1, n - 1)%self.mod + \
                    self.f(x + 2, y + 1, n - 1)%self.mod + \
                    self.f(x + 1, y - 2, n - 1)%self.mod + \
                    self.f(x - 1, y - 2, n - 1)%self.mod + \
                    self.f(x - 2, y + 1, n - 1)%self.mod + \
                    self.f(x - 2, y - 1, n - 1)%self.mod + \
                    self.f(x + 1, y + 2, n - 1)%self.mod + \
                    self.f(x - 1, y + 2, n - 1)%self.mod 
                
        self.dp[(x, y, n)] = retval
        return retval
    
    
    def knightDialer(self, n: int) -> int:
        
        phone_pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        
        self.dp = {}
        self.mod = 10**9 + 7
        
        op = 0
        for i in range(4):
            for j in range(3):
                retval = self.f(i, j, n)
                # print(i, j, retval)
                op = (op + retval)%self.mod
                
        return op
                
        
        
        
        