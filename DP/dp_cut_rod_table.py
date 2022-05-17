import sys

class Solution:
    
    def cutRod(self, price, n):
        #code here
        dp = [0] * (n + 1)
        for rod in range(1, n + 1):
            for index  in range(len(price)):
                if index + 1 <= rod:
                    max_val = dp[rod - index - 1]
                    if dp[rod] < max_val + price[index]:
                        dp[rod] = max_val + price[index]
                        
        return dp[n]
        
        
        
    
if __name__ =='__main__':
    print(Solution().cutRod([1, 3, 3, 3, 4, 4, 6], 7))