class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages = sorted(ages)
        L = len(ages)
        count = 0
        
        for i in range(0, L):
            lb = ages[i]
            ub = (ages[i] - 7)*2
            
            l = bisect.bisect_left(ages, lb)
            h = bisect.bisect_left(ages, ub)
            
            # print(l, h)
            if h - l <= 0:
                continue
                
            count += h - l
            
            if lb <= ages[i] < ub:
                count -= 1
            
                
        return count