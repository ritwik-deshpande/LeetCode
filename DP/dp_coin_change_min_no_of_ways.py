import sys
class Solution:
    
    def f(self, coins, no_of_coins, amount):
       
        if (amount, no_of_coins) in self.dp:
            return self.dp[(amount, no_of_coins)]
        
        
        if amount == 0 :
            return 0
            
        if no_of_coins <= 0:
            return sys.maxsize
        
        
        
        if coins[no_of_coins - 1] <= amount:
            retval_1 = 1 + self.f(coins, no_of_coins, amount - coins[no_of_coins - 1])
            retval_2 = self.f(coins, no_of_coins - 1,  amount)
            self.dp[(amount, no_of_coins)] = min(retval_1, retval_2)
            return self.dp[(amount, no_of_coins)]
        else:
            self.dp[(amount, no_of_coins)] = self.f(coins, no_of_coins - 1,  amount)
            return self.dp[(amount, no_of_coins)]
        
    
    def change(self, amount, coins) :
        self.dp = {}
        self.combinations = []
        retval = self.f(coins, len(coins), amount)
        return retval
        
        
        
    
if __name__ =='__main__':
    print(Solution().change(10, [1,3,4,6,8]))