class Solution:
        
        
    
    def videoStitching(self, clips, time) :
        l = 0
        r = 0
        N = len(clips)
        steps = 0
        
        jump = {}
        for beg, end in clips:
            if beg not in jump:
                jump[beg] = end
            else:
                jump[beg] = max(jump[beg], end)
        end = 0
        
        while r < time:
            i = l
            clip_found = False
            while i < r+1:
                if i in jump:
                    end = max(end, jump[i])
                    clip_found = True
                i = i + 1
                  
            if not clip_found:
                return -1
            
            l = r+1
            r = end
            steps = steps + 1
            
        return steps