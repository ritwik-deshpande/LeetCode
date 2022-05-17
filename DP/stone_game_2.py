class Solution:
    def f(self, n, M, play):
        # print(n, M, play)
        
        if (n, M, play) in self.dp:
            return self.dp[(n, M, play)]
        
        if n == self.L:
            return 0
        
        if play == 'Alice':
            res_a = float('-inf')
            sum_a = 0
            for x in range(1, 2*M + 1):
                if n + x - 1 >= self.L:
                    break
                sum_a = sum_a + self.piles[n + x - 1]
                
                op = self.f(n + x, max(x, M), "Bob")
                res_a = max(res_a, op + sum_a)
                
                # print("Alice op ", res_a)
            
            retval =  res_a
                
        else:
            res_b = float('inf')
            for x in range(1, 2*M + 1):
                if n + x - 1 >= self.L:
                    break
                
                res_b = min(res_b, self.f(n + x, max(x, M), "Alice"))
                
                # print("Bob response op ", res_b)    
            
            retval =  res_b
        
        self.dp[(n, M, play)] = retval
        return retval
    
    
    def stoneGameII(self, piles: List[int]) -> int:
        
        self.dp = {}
        self.piles = piles
        self.L = len(piles)
        return self.f(0, 1, 'Alice')