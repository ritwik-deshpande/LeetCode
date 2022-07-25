class Solution:
    
    
    def f(self, i, op, x):
        
        if (i, op, x) in self.dp:
            return self.dp[(i, op, x)]
        
        if x > self.k:
            return 0
        
        if i >= self.n:
            return 0
        
        if op == 'buy':
            
            ret = max(self.f(i + 1, 'sell', x + 1)  - self.prices[i],  self.f(i + 1, 'buy', x))
        
        else:
            ret = max(self.f(i + 1, 'buy', x)  + self.prices[i],  self.f(i + 1, 'sell', x))
            
        self.dp[(i, op, x)] = ret
        return ret
    
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.dp = {}
        self.n = len(prices)
        self.k = 2
        
        return self.f(0, 'buy', 0)
        