class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(lambda s: int(s), str(n)))
        L = len(nums)
        if L == 1:
            return -1
        
        
        idx = -1
        
        for i in range(L - 1, 0, -1):
            # print(i)
            if nums[i] > nums[i - 1]:
                idx = i - 1
                break
                
        if idx == -1:
            return -1
        
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
            
        nums = list(map(lambda n: str(n), nums))
        op = int(''.join(nums))
        
        if op > 2**31 - 1:
            return -1
        
        return op
        