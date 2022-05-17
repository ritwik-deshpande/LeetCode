
class Solution:
    
    def f(self, W, n):
        
        if (W, n) in self.dp:
            return self.dp[(W,n)]
        
        if W == 0 or n == 0:
            return 0, []
            
        
        if self.wt[n - 1] <= W:
            cost_1, combination_1 = self.f(W - self.wt[n - 1], n - 1) 
            cost_1 = cost_1 + self.val[n - 1]
            combination_1 = combination_1 + [self.wt[n - 1]]
            cost_2, combination_2 = self.f(W, n - 1)
            max_cost = max(cost_1, cost_2)
            if max_cost == cost_1:
                optimal_combination = combination_1
            else:
                optimal_combination = combination_2
            self.dp[(W,n)] = (max(cost_1, cost_2), optimal_combination)
            
        else:
            self.dp[(W,n)]  = self.f(W, n - 1)
        return self.dp[(W,n)]
        
        
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        self.val = val
        self.wt = wt
        self.dp = {}
        retval =  self.f(W, n)
        print(retval)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends