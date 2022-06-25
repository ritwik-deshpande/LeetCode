class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        
        L = len(nums)
        for _ in range(L - k + 1):
            n = heapq.heappop(nums)
            
        return n
