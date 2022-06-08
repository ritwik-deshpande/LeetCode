class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr = sorted(arr)
        L = len(arr)
        min_diff = min([ arr[i] - arr[i - 1] for i in range(1, L)])
        
        ans = []
        
        for i in range(1, L):
            if arr[i] - arr[i - 1] == min_diff:
                ans.append([arr[i -1], arr[i]])
                
        return ans
        