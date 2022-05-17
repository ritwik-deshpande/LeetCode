class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_so_far = float('-inf')
        retval = float('-inf')
        
        for num in nums:
            max_so_far = max(num, num + max_so_far)
            if retval < max_so_far:
                retval = max_so_far
        
        return retval