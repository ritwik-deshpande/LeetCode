class Solution:
    
#     def f(self, l, r):
#         if l >= r:
#             return
        
#         if self.nums[l] + self.nums[r] == self.target:
#             self.ans = [l+1, r+1]
#             return
        
#         # if self.nums[l] + self.nums[r] > self.target:
#         self.f(l, r - 1)
#         self.f(l + 1, r)
            
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers[r] < target:
                l = l + 1
                
            elif numbers[l] + numbers[r] > target:
                r = r - 1
                
            else:
                ans = [l + 1, r + 1]
                break
                
        return ans
            