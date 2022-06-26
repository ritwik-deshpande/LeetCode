class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        stack = []
        
        for num in nums[::-1]:
            while stack and stack[0] <= num:
                stack.pop(0)
                
            stack.insert(0, num)
            
        # print(stack)
        L = len(nums)
        ans = []
        # reducing time complexity from n^2 to 2n
        for i in range(L - 1, -1, -1):
            if nums[i] < stack[0]:
                ans.append(stack[0])
                
            else:
                
                while stack and stack[0] <= nums[i]:
                    stack.pop(0)
                    # print(stack[0], nums[i])
                
                # print(stack)
                if stack:
                    ans.append(stack[0])
                else:
                    ans.append(-1)
                    
            stack.insert(0, nums[i])
            # print(ans)
        return ans[::-1]
                                
        