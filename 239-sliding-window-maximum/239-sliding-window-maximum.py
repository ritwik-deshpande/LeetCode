class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        q = []
        ans = []
        L = len(nums)
        i = 0
        while i < L:
            
            
            while q and q[-1][0] < nums[i]:
                q.pop()

            
            q.append((nums[i], i))
            # print(q, i)
                
            
            if i >= k - 1:
                ans.append(q[0][0])
                while q and q[0][1] <= i - k + 1:
                    q.pop(0)
                
            i += 1
            
        return ans
        
            
            
            
            