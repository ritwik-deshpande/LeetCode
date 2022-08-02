class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        pos = [0, 0]
        face = 0
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        
        
        for ch in instructions:
            
            if ch == 'L':
                face = (face - 1)%4
                
            elif ch == 'R':
                face = (face + 1)%4
                
            else:
                pos[0] += dirs[face][0]
                pos[1] += dirs[face][1]
            # print(ch, face, pos)
            
            
        if (pos[0] == 0 and pos[1] == 0) or face != 0:
            return True
        
        return False
            
                
        
        
        