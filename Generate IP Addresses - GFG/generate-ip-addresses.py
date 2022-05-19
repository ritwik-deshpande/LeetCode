#Your Function should return a list containing all possible IP address
#No need to worry about order
class Solution:
    def f(self, index, ip, dot):
        if dot == 3:
            sub_ip = self.s[index: ]
            if len(sub_ip) > 0 and int(sub_ip) >= 0 and int(sub_ip) <= 255:
                if len(sub_ip) > 1 and sub_ip[0] == '0':
                    return
                ip = ip + sub_ip
                self.ans.append(ip)
            
        
        for i in range(index + 1, self.L):
            sub_ip = self.s[index: i]
            # print(sub_ip)
            if len(sub_ip) > 0 and int(sub_ip) >= 0 and int(sub_ip) <= 255:
                if len(sub_ip) > 1 and sub_ip[0] == '0':
                    continue
                self.f(i, ip + sub_ip + '.', dot + 1)
                
        
        
        
    
    def genIp(self, s):
        #Code here
        self.ans = []
        self.s = s
        self.L = len(s)
        self.f(0, '', 0)
        
        return self.ans

#{ 
#  Driver Code Starts
#Main
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        if(len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
# } Driver Code Ends