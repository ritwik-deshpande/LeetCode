class Solution:
    def f(self, N):
        
        # print(N)
        if N in self.dp:
            return self.dp[N]
        if N == 0:
            return 1
        
                
        cost = 1
        for i in self.nums:
            if i <= N:
                retval = self.f(N - i)*i
                cost = max(cost, retval)
                
        self.dp[N] = cost
                
        return cost
    
    
    def integerBreak(self, n: int) -> int:
        
        self.nums = [ i for i in range(1, n)]
        # print(self.nums)
        self.dp = {}
        
        return self.f(n)
        