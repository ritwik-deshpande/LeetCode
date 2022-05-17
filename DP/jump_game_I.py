class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        jump_range = [ (i, i+num) for i, num in enumerate(nums)]
        
        
        end = 0
        N = len(nums) 
        jump_possible = False
        for i in range(N):
            jump_possible = False
            if jump_range[i][0] <= end:
                if end < jump_range[i][1]:
                    end = jump_range[i][1]
                jump_possible = True
            
            if not jump_possible:
                return False

            if end == N - 1:
                return True
            
        return True