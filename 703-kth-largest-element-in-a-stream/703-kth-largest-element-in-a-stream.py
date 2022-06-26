class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        idx = bisect.bisect_left(self.nums, val)
        
        self.nums = self.nums[:idx] + [val] + self.nums[idx:]
        
        # print(self.nums)
        
        return self.nums[len(self.nums) - self.k]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)