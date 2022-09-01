class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        L = len(nums)
        
        ans = []
        for n, v in d.items():
            
            if v > math.floor(L//3):
                ans.append(n)
                
        return ans