class Solution(object):
    def f(self, ptr, target, path, k):
        
        if target == 0 and k == self.k:
            self.ans.append(path)
            
        if ptr == self.N or target < 0 or  k > self.k:
            return
    
        
            
        
        for i in range(ptr, self.N):
            
            self.f(i + 1, target - self.nums[i], path + [self.nums[i]], k + 1)
            
        
    
    def combinationSum3(self, k, n):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = range(1, 10)
        self.N = len(self.nums)
        self.ans = []
        self.k = k
        self.f(0, n, [], 0)

        return self.ans
        