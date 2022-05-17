class Solution:
    
    def f(self, amount):
       
        if amount in self.dp:
            # self.dp[(amount, no_of_coins)] = self.dp[(amount, no_of_coins)] + 1
            return self.dp[amount]
        
        
        if amount == 0:
            return 1
            
        if amount < 0:
            return 0
            
        cnt = 0
        for i in range(len(self.coins)):
            
            cnt = cnt + self.f(amount - self.coins[i])
            
        self.dp[amount] = cnt
        return self.dp[amount]
    
    def combinationSum4(self, coins, amount) :
        self.dp = {}
        self.coins = coins
        self.combinations = []
        retval = self.f(amount)
        print(self.dp)
        return retval
    # def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        
        

if __name__ == '__main__':
    print(Solution().combinationSum4([1,2,3], 4))