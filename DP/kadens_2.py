class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_positive = nums[0]
        max_negative = nums[0]
        retval = nums[0]
        
        for num in nums[1:]:
            temp = max(max(num, max_positive*num), num*max_negative)
            max_negative = min(min(num, max_positive*num), num*max_negative)
            max_positive = temp
            retval = max(retval, max(max_positive, max_negative))
            print(max_positive, max_negative, retval)
                
        return retval
        
        