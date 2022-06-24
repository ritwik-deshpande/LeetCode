class Solution:
            
        
        
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Find first point where nums are not sorted in descending order
        
        L = len(nums)
        if L == 1:
            return 
        
        if L == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        
        idx = -1
        
        for i in range(L - 1, 0, -1):
            # print(i)
            if nums[i] > nums[i - 1]:
                idx = i - 1
                break
                
        if idx == -1:
            nums.sort()
            return 
        # print("the idx is", idx)
        next_greatest_num = float('inf')
        for j in range(idx, L):
            if nums[j] > nums[idx]:
                if nums[j] < next_greatest_num:
                    idx_j = j
                    next_greatest_num = nums[j]
                    
                    
        nums[idx], nums[idx_j] = nums[idx_j], nums[idx]
        
        sorted_nums = sorted(nums[idx + 1:])
        
        j = 0
        for i in range(idx + 1, L):
            nums[i] = sorted_nums[j]
            j += 1
        
                
                
            
        
        
        
        
        