class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        ans = 0
        for price in prices[1:]:
            
            profit = price - buy
            ans += max(0, profit)

            buy = price
            
        return ans
            
            
            
        