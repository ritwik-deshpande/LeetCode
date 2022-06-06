class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        L = len(nums)
        while i < L - 1:
            
            j = i
            c = 1
            while j < L - 1 and nums[j] == nums[j + 1] :
                if c > 1:
                    nums[j] = '_'
                c = c + 1
                j += 1
                
                
            i = j + 1
            
        print(nums)
        
        idx = 0
        for num in nums:
            
            if num != '_':
                nums[idx] = num
                idx += 1
                
            
        return idx
        