class Solution(object):
   
    
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        time = sorted([t%60 for t in time])
        # print(time)
        cache = collections.defaultdict(int)
        val = 60
        ans = 0
        for t in time:
            
            if val - t in cache:
                ans += cache[val - t]
                
            cache[t] += 1
                
            # print(cache)
            
            
        cache = collections.defaultdict(int)
        val = 0
        for t in time:
            
            if val - t in cache:
                ans += cache[val - t]
                
            cache[t] += 1
                
            # print(cache)
            
        
               
        return ans
        