class Solution:
    def f(self, n, M, N):
        if (n, M, N) in self.dp:
            return self.dp[(n, M, N)]
        if n == 0:
            return 0
            
        if M == 0 and N == 0:
            return 0

        if self.str_values[n - 1][0] <= M and self.str_values[n - 1][1] <= N:
            retval_1 = self.f(n - 1, M - self.str_values[n - 1][0], N - self.str_values[n - 1][1]) + 1
            retval_2 = self.f(n - 1, M, N)
            
            self.dp[(n, M, N)] = max(retval_1, retval_2)
            return self.dp[(n, M, N)]
            
        else:
            self.dp[(n, M, N)] = self.f(n - 1, M, N)
            return self.dp[(n, M, N)]

    def findMaxForm(self, strs, m, n):
        self.dp = {}
        
        self.str_values = [(list(string).count('0'), list(string).count('1')) for string in strs]
        print(self.str_values)
        retval = self.f(len(strs), m, n)
        print(self.dp)
        return retval
        
        
        
        
            
if __name__ == '__main__':
    print(Solution().findMaxForm(["10","1","0"], 1, 1))