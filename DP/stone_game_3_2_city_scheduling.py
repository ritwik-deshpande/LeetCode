class Solution:
            
    
    
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
        pairs = [(a, b)  for a, b in zip(aliceValues, bobValues)]
        
        pairs = sorted(pairs, key = lambda x : x[0] + x[1], reverse = True)
        print(pairs)
        
        sum_a = 0
        sum_b = 0
        for i in range(len(pairs)):
            if i%2 == 0:
                sum_a = sum_a + pairs[i][0]
            else:
                sum_b = sum_b + pairs[i][1]
                
        if sum_a > sum_b:
            return 1
        elif sum_b > sum_a:
            return -1
        
        return 0
                
            
                
            