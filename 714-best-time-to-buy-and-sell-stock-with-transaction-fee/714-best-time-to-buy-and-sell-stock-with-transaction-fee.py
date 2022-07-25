class Solution:
    
    def f(self, i, op):
        
        if (i, op) in self.dp:
            return self.dp[(i, op)]
        
        if i >= self.n:
            return 0
        
        if op == 'buy':
            
            ret = max(self.f(i + 1, 'sell')  - self.prices[i],  self.f(i + 1, 'buy'))
        
        else:
            ret = max(self.f(i + 1, 'buy')  + self.prices[i] - self.fee,  self.f(i + 1, 'sell'))
            
        self.dp[(i, op)] = ret
        return ret
            
            
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        self.fee = fee
        self.prices = prices
        self.n = len(prices)
        self.dp = {}
        
        return self.f(0, 'buy')