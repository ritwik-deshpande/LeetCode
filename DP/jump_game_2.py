class Solution:
        
    def videoStitching(self, clips, time):
        start = 0
        end = 0
        index = 0
        N = len(clips)
        required_clips = []
        clips = sorted(clips, key = lambda x: x[0])
        print(clips)
        
        while end < time:
            start = end
            clip_found = False
            for i in range(index, N):
                if clips[i][0] <= start and end < clips[i][1]:
                    end = clips[i][1]
                    index = i
                    best_clip = clips[i]
                    clip_found = True
                    
                  
            if not clip_found:
                return -1
            required_clips.append(best_clip)
         
        print(required_clips)           
        return len(required_clips) 
        
        
if __name__ =='__main__':
    slots = [True]*10
    
    # print(slots[:0])
    
    # slots[2:7] = [False]*5
    # print(slots)
    
    print(Solution().videoStitching([[0,5],[6,8]], 7))
    
    print(Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))
    print(Solution().videoStitching([[0,1],[1,2]], 10))