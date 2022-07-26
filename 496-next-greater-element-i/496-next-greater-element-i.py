class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        stack = []
        next_greater = [-1 for _ in range(len(nums2))]
        for i, num in enumerate(nums2):
            
            while stack and stack[-1][0] < num:
                _, j = stack.pop()
                next_greater[j] = num
                j += 1
                
            stack.append((num, i))
            
        ans = []
        for num in nums1:
            idx = nums2.index(num)
            ans.append(next_greater[idx])
            
        return ans
            
            
            