from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        sorted_nums = SortedList(nums)
        ans = []
        for num in nums:
            ans.append(sorted_nums.index(num))
            sorted_nums.remove(num)
            
        return ans
            
            
            
        