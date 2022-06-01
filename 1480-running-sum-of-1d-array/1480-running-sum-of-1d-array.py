class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        s = 0
        for i, num in enumerate(nums):
            s = s + num
            nums[i] = s
            
        return nums
            