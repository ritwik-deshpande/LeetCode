class Solution:
    
    def get_primes(self, n):
        
        primes = [True for i in range(n+1)]
        p = 2
        while p*p <= n :
            if primes[p] == True:
                for i in range(p*p, n+1, p):
                    primes[i] = False
            p = p + 1
           
        return [index  for index, value in enumerate(primes) if value == True and index != 0]
        
    
    def minSteps(self, n):
        primes = self.get_primes(1000)
        retval = 0
        i = 1
        while n != 1:
            if n%primes[i] == 0:
                n = n/primes[i]
                retval = retval + primes[i]
            else:
                i = i + 1
        return retval
        
if __name__ == '__main__':
    print(Solution().minSteps(700))