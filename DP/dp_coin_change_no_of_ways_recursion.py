class Solution:
    
    def f(self, coins, no_of_coins, combination, amount):
       
        if no_of_coins <= 0:
            return 
        
        if amount == 0:
            self.combinations.append(combination)
            return 
        
        if amount < 0 :
            return
        
        new_combination = combination + [coins[no_of_coins - 1]]
        self.f(coins, no_of_coins, new_combination, amount - coins[no_of_coins - 1])
        self.f(coins, no_of_coins - 1, combination,  amount)
        return
    
    def change(self, amount, coins) :
        self.dp = {}
        self.combinations = []
        self.f(coins, len(coins), [], amount)
        return len(self.combinations)
        
        
        
    
if __name__ =='__main__':
    print(Solution().coinChange([1,3,4,6,8], 10))