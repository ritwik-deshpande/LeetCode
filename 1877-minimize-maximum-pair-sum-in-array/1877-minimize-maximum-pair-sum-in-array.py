class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        L = len(nums)
        
        return max([nums[i] + nums[L - i - 1] for i in range(0, L//2) ])
            