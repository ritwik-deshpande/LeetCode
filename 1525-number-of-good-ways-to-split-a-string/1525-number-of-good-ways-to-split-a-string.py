class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        cnt = []
        cache = []
        c = 0
        for ch in s:
            if ch not in cache:
                c += 1
                cache.append(ch)
            
            cnt.append(c)
          
        rev_cnt = []
        cache = []
        c = 0
        for ch in s[::-1]:
            if ch not in cache:
                c += 1
                cache.append(ch)
            
            rev_cnt.append(c)
            
    
        rev_cnt = rev_cnt[::-1]
        # print(cnt, rev_cnt)
        ans = 0
        total_cnt = c
        for i in range(len(cnt) - 1):
            if cnt[i] == rev_cnt[i + 1]:
                
                ans += 1
            
                
        return ans
                
            
        