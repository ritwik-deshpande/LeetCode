class Solution:
    
    def canCatchUp(self, p1, s1, p2, s2):
        # print(p1, s1, p2, s2)
        
        if s2 - s1 == 0:
            return -1
        
        t = (p1 - p2)/(s2 - s1)
        return t
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        self.target = target
        pos_speed = [(pos, s)   for pos, s in zip(position, speed)]
        
        pos_speed = sorted(pos_speed, key=lambda x : (x[0], x[1]), reverse=True)
        
        # print(pos_speed)
        
        stack = [(pos_speed[0][0], pos_speed[0][1])]
        for pos, s in pos_speed[1:]:
            top = stack[-1]
            
            if (self.target - top[0])/top[1] >= (self.target - pos)/s:
                pass
                # stack.pop()
                # stack.append((pos, s))
                
            else:
                stack.append((pos, s))
                
            # print(stack)
                
                
        return len(stack)
                
                
            
            
            
            
            
        
        