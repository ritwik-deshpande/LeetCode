class Solution:
    
    def f(self, left, right):
        
        
        if left >= right:
            return 0
        
        if (left, right) in self.dp:
            return self.dp[(left, right)]

        ans = float('inf')
        
        for i in range(left, right):
            retval_1 = self.f(left, i - 1)
            # print(f"left branch for root {i} cost {retval_1}")
            retval_2 = self.f(i + 1, right)
            # print(f"Right branch for root {i} cost {retval_2}")
            ans = min(ans, max(retval_1, retval_2) + i)
            
        self.dp[(left, right)] = ans
    
        return ans
    
    def getMoneyAmount(self, n: int) -> int:
        
        self.dp = {}
        
        return self.f(1, n)
        