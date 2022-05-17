class Solution:
    
    def f(self, index, label):
        if (index, label) in self.dp:
            return self.dp[(index, label)]
            
        # print(self.nums[index-1], label)
        
        if index == self.L:
            return 0
        
        prev = self.nums[index - 1]
        max_l = 0
        for i in range(index, self.L):
            if (self.nums[i] - prev > 0 and label > 0) or (self.nums[i] - prev < 0 and label < 0):
                retval = self.f(i + 1, label*(-1)) + 1
                max_l = max(max_l, retval)
                
        # print(max_l, self.nums[index], label)
        self.dp[(index, label)] = max_l
        return max_l
            
    
    
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        self.nums = nums
        self.L = len(nums)
        
        self.dp = {}
        
        retval_1 =  self.f(1, 1)
        
        retval_2 = self.f(1, -1)
        
        
        return max(retval_1, retval_2) + 1
        
        
        