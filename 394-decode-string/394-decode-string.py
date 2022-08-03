class Solution(object):
    
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        

        stack = []
        
        i = 0
        L = len(s)
        
        while i < L:
            
            
            if s[i] == ']':
                
                new_s = ''
                while stack and stack[-1] != '[':
                    ch = stack.pop()
                    new_s = ch + new_s
                _ = stack.pop()
                dig = ''
                while stack and stack[-1].isnumeric():
                    d = stack.pop()
                    dig = d + dig
                num = int(dig)
                new_s = new_s
                stack.append(new_s*num)
                
            else:
                stack.append(s[i])
            # print(stack)

            i += 1
            
        ans = ''
        for ele in stack:
            ans += ele
        return ans