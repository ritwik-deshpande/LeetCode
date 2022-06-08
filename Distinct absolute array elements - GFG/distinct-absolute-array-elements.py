

class Solution:
    def distinctCount(self, arr, n):
        # code here
        
        l = 0
        r = n - 1
        cnt = 0
        while l <= r:
            
            while l < r and r > 0 and arr[r - 1] == arr[r]:
                r = r - 1
                    
            while l < r and l < n - 1 and arr[l] == arr[l + 1]:
                l = l + 1
            
            if abs(arr[l]) == abs(arr[r]):
                l = l + 1
                r = r - 1
                
                
            elif abs(arr[l]) > abs(arr[r]):
                l = l + 1
                
            else:
                r = r - 1
                
            cnt = cnt + 1
            
        return cnt
            
                
                
        

#{ 
#  Driver Code Starts





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.distinctCount(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends