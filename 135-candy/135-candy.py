class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        L = len(ratings)
        candies = [1 for _ in range(L)]
        
        
        for i in range(1, L):
            
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        
        for i in range(L - 1):
            
            if ratings[L - i - 1] < ratings[L - i - 2]:
                if candies[L - i - 1] >= candies[L - i - 2]:
                    candies[L - i - 2] = candies[L - i - 1] + 1
                    
                    
        return sum(candies)
                
        
        