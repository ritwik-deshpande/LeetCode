class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        store = []
        nums = sorted(nums)
        s = 0
        for i, num in enumerate(nums):
            s += num
            store.append(s)
            
            
        
        ans = []
        
        for q in queries:
            idx = bisect.bisect_right(store, q)
            # print(q, idx, store)
            ans.append(idx)
            
        return ans
            
        
        