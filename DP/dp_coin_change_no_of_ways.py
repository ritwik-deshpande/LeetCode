class Solution:
    
    def f(self, coins, no_of_coins, amount):
       
        if (amount, no_of_coins) in self.dp:
            return self.dp[(amount, no_of_coins)]
        
        
        if amount == 0:
            return 1
            
        if no_of_coins <= 0 :
            return 0
            
        if coins[no_of_coins - 1] <= amount:
            retval_1 = self.f(coins, no_of_coins, amount - coins[no_of_coins - 1])
            retval_2 = self.f(coins, no_of_coins - 1,  amount)
            self.dp[(amount, no_of_coins)] = retval_1 + retval_2
            return self.dp[(amount, no_of_coins)]
        else:
            self.dp[(amount, no_of_coins)] = self.f(coins, no_of_coins - 1,  amount)
            return self.dp[(amount, no_of_coins)]
        
    
    def combinationSum4(self, coins, amount) :
        self.dp = {}
        self.combinations = []
        retval = self.f(coins, len(coins), amount)
        print(self.dp)
        return retval
    # def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        
        

if __name__ == '__main__':
    print(Solution().combinationSum4([1,2,3], 4))