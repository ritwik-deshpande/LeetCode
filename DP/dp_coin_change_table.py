import sys

class Solution:
    
    def f(self, coins, no_of_coins, combination, amount):
        
        dp = [sys.maxsize]*(amount + 1)
        dp[0] = 0
        
        for value in range(1, amount + 1):
            for index in range(0, len(coins)):
                if coins[index] <= value:
                    min_val = dp[value - coins[index]]
                    if min_val != sys.maxsize and min_val + 1 < dp[value]:
                        dp[value] = min_val + 1
        # print(dp)
        return dp[amount]
            
    
    def change(self, amount, coins) :
        self.dp = {}
        self.combinations = []
        self.optimal_val = sys.maxsize
        ans = self.f(coins, len(coins), [], amount)
        return ans
        
        
        
    
if __name__ =='__main__':
    print(Solution().change(27, [2,5,10,1]))