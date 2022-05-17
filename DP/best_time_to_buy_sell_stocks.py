# cook your dish here
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_val = float('inf')
        max_profit = 0
        for num in prices:
            if min_val > num:
                min_val = num
                
            print(num, min_val, max_profit)
            max_profit = max(num - min_val, max_profit)
                
        return max_profit