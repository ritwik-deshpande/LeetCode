class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        count = [1]*len(nums)
        LIS = [1]*len(nums)
        
        for i in range(1, len(nums)):
            max_cnt = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    # print(nums[j], nums[i])
                    # LIS[i] = max(LIS[i], LIS[j] + 1)
                    
                    # print(LIS[i], LIS[j], nums[i], nums[j])
                    if LIS[i] < LIS[j] + 1:
                        count[i] = count[j]
                        LIS[i] = LIS[j] + 1
                    elif LIS[i] == LIS[j] + 1:
                        # print("hi")
                        count[i] = count[i] + count[j]
                        # print(count[i])
                  
                        
                      
        # count[1] = len(nums)
        print(count)   
        max_val = max(LIS)
        index = LIS.index(max_val)
        
        ans = 0
        
        for i in range(len(LIS)):
            if LIS[i] == max_val:
                ans = ans + count[i]
        
        
        return ans
                
        