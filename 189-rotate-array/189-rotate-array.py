class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        k = k%L
        
        op =  nums[L - k:] + nums[:L - k]
        
        # print(op)
        for i, num in enumerate(op):
            nums[i] = num
            
        