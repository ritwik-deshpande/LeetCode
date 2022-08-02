class Solution(object):
    
    
    def f(self, ptr, target, path):
        
            
        if ptr == self.N or target < 0:
            return
    
        if target == 0:
            self.ans.append(path)
            
        
        for i in range(ptr, self.N):
            
            self.f(i, target - self.nums[i], path + [self.nums[i]])
            
        
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = candidates
        self.N = len(self.nums)
        self.ans = []
        
        self.f(0, target, [])

        return self.ans