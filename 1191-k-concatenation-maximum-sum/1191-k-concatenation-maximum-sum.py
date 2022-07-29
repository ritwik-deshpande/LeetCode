class Solution:
    
    def findMaxSum(self, arr):
        max_so_far = 0
        m = 0
        for num in arr:
            max_so_far = max(0, max_so_far + num)
            m = max(m, max_so_far)
            
        return m
    
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        if k == 1:
            return self.findMaxSum(arr)%(10**9 + 7)
        if k == 2:
            return self.findMaxSum(arr + arr)%(10**9 + 7)
            
            
        new_arr = []
        k -= 1
        new_arr = arr + arr
      
        s1 = self.findMaxSum(new_arr)
        
        new_arr = new_arr + arr
        k -= 1
        
        s2 = self.findMaxSum(new_arr)
        # print(s1, s2)
        if s1 == s2:
            return s1%(10**9 + 7)
        
        else:
            s = s1 + (k)*(s2 -s1)
            return s%(10**9 + 7)
        