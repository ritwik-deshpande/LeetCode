class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        diff = []
        prev = 0
        for t in releaseTimes:
            
            diff.append(t - prev)
            prev = t
            
    
        ans = 'a'
        max_t = max(diff)
        
        for i, t in enumerate(diff):
            if t == max_t:
                ans = max(ans, keysPressed[i])
                
        return ans