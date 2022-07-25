class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        try:
        
            _ = nums.index(target)
            l = bisect.bisect_left(nums, target)

            r = bisect.bisect_right(nums, target) - 1
        
        except Exception as e:
            return [-1, -1]
        
        return [l, r]
        