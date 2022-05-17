class Solution:
    
    def f(self, index, k):
        if (index, k) in self.dp:
            return self.dp[(index, k)]
        if index == self.n and k == 0:
            return 0
        
        if index >= self.n or k <= 0:
            return float("-inf")
        
        total = 0
        max_average = 0
        size = 0.0
        combo = []
        for partition in range(index, self.n):
            size += 1.0
            total += self.nums[partition]
            combo = combo + [self.nums[partition]]
            # print(combo, k)
            max_average = max(max_average, (total/size) + self.f(partition+1, k-1))
            # print(combo, max_average, k)
        self.dp[(index, k)] = max_average
        return max_average
        
        
    def largestSumOfAverages(self, nums, k):
        self.dp = {}
        self.n = len(nums)
        self.nums = nums
        return self.f(0,k)
           

        
        
if __name__ =='__main__':
    print(Solution().largestSumOfAverages([4,1,7,5,6,2,3], 4))
    print(Solution().largestSumOfAverages([1,2,3,4,5,6,7], 4))
    print(Solution().largestSumOfAverages([9,1,2,3,9], 3))