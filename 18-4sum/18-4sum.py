class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        
        L = len(nums)
        ans = []
        for i in range(L):
            for j in range(i + 1, L):
                
                l = j + 1
                r = L - 1
                
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r] 
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        if [nums[i], nums[j], nums[l], nums[r]] not in ans:
                            ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                    
        return ans
                    
                    