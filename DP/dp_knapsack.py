class Solution:
    
    def f(self, W, n):
        
        if (W, n) in self.dp:
            return self.dp[(W,n)]
        
        if W == 0 or n == 0:
            return 0
            
        
        if self.wt[n - 1] <= W:
            cost_1 = self.val[n - 1] + self.f(W - self.wt[n - 1], n - 1)
            cost_2 = self.f(W, n - 1)
            self.dp[(W,n)] = max(cost_1, cost_2)
            
        else:
            self.dp[(W,n)]  = self.f(W, n - 1)
        return self.dp[(W,n)]
