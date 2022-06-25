class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        i = 1
        j = 0
        count = 0
        while i < len(nums):
            
            if nums[i - 1] > nums[i]:
                count += 1
                j = i - 1
                
            i += 1
        
        if count > 1:
            return False
        
        
        if j == 0 or j + 1 == len(nums) - 1:
            return True
        
        if (nums[j - 1] <= nums[j + 1]) or (nums[j] <= nums[j + 2]) :
            return True
        
        return False
            
            
        