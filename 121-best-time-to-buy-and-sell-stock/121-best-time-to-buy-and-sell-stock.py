class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            
            buy = min(price, buy)
            
            profit = max(profit, price - buy)
            
        return profit
        