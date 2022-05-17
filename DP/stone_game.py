class Solution:
    
    def f(self, left, right):
        
        
        if left > right:
            return 0
        
        if (left, right) in self.dp:
            return self.dp[(left , right)]
        
        op1 = self.f(left + 2, right) + self.piles[left]
        op2 = self.f(left + 1, right - 1) + self.piles[left]
        
        op3 = self.f(left, right - 2) + self.piles[right]
        op4 = self.f(left + 1, right - 1) + self.piles[right]

        
        
        retval = max( min(op1, op2), min(op3, op4))
        
        self.dp[(left , right)] = retval
        return retval
        
    
    
    
    def stoneGame(self, piles: List[int]) -> bool:
        
        self.piles = piles
        self.dp = {}
        s = sum(piles)
        op =  self.f(0, len(piles) - 1)
        print(op)
        
        if op > s - op:
            return True
        return False
        