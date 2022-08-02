class Solution(object):
    def f(self, ptr, target, path):
        
        if (ptr, target, tuple(path)) in self.dp:
            return
        if target == 0:
            if path not in self.ans:
                self.ans.append(path)
            
        if ptr == self.N or target < 0:
            return
    
        for i in range(ptr, self.N):
            
            self.f(i + 1, target - self.nums[i], path + [self.nums[i]])
        
            self.dp[(ptr, target, tuple(path))] = True
        
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = sorted(candidates)
        self.N = len(self.nums)
        self.ans = []
        self.dp = {}
        
        self.f(0, target, [])

        return self.ans
        