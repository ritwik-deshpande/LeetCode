class Solution(object):
    
    def numberOfWays(self, s):
        n = len(s)

        right_zeros = s.count("0")
        right_ones = n - right_zeros

        result, left_zeros, left_ones = 0, 0, 0

        for i in range(n):
            if s[i] == "1":
                result += left_zeros*right_zeros
                left_ones += 1
                right_ones -= 1
            else:
                result += left_ones*right_ones
                left_zeros += 1
                right_zeros -= 1

        return result
        
        