class Solution:
    
    def rob(self, nums):
        
        dp = [(num, [index]) for index, num in enumerate(nums)]
        
        dp_wo_zero = [(num, [index]) for index, num in enumerate(nums)]
        
        for i in range(0, len(nums) - 1):
            for j in range(0, i):
                if abs(j - i) != 1  :
                    max_score = max(dp[i][0], dp[j][0] + nums[i])
                    
                    if max_score == dp[i][0] :
                        combination = dp[i][1]
                    else:
                        combination = dp[j][1] + [i]
                    dp[i] = (max_score, combination)
                    
        for i in range(1, len(nums)):
            for j in range(1, i):
                if abs(j - i) != 1  :
                    max_score = max(dp_wo_zero[i][0], dp_wo_zero[j][0] + nums[i])
                    
                    if max_score == dp_wo_zero[i][0] :
                        combination = dp[i][1]
                    else:
                        combination = dp_wo_zero[j][1] + [i]
                    dp_wo_zero[i] = (max_score, combination)
        

        
        return max([score for score, _ in dp] + [score for score, _ in dp_wo_zero])
        
        
            
if __name__ == '__main__':
    print(Solution().rob([2,1,2,6,1,8,10,10]))