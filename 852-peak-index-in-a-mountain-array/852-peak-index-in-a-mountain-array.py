class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_ele = max(arr)
        
        return arr.index(max_ele)

        