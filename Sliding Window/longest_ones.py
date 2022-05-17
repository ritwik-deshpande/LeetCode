class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        
        i = 0 
        j = 0
        count_of_zero = 0
        
        L = len(nums)
        window = 0
        
        while i < L:
            
            if nums[i] == 0:
                count_of_zero = count_of_zero + 1
                
            while count_of_zero > k and j < L:
                if nums[j] == 0:
                    count_of_zero = count_of_zero - 1
                j = j + 1
                
            
            window = max(window, i - j + 1)
            i = i + 1
            
        return window   