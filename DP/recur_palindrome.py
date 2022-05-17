class Solution:
    # @param A : string
    # @return a list of list of strings
    
    def isPalindrome(self, s):
        str_len = len(s)
        if str_len == 1:
            return True
        # print(str_len//2)
        if str_len%2 == 0:
            first_half = s[0: str_len//2]
            second_half = s[str_len//2 :]
            second_half = second_half[::-1]
            
            print(first_half, second_half)
            if first_half == second_half:
                return True
        
        if str_len%2 == 1:
            first_half = s[0: str_len//2]
            second_half = s[str_len//2 + 1 :]
            second_half = second_half[::-1]
            print(first_half, second_half)
            if first_half == second_half:
                return True
        return False
    
    def f(self, index, combination):
        if index == len(self.A):
            self.combinations.append(combination)
            return 
        
        
        for partition in range(index + 1, len(self.A) + 1):
            possible_palindrome = self.A[index : partition]
            print("possible palindrome", possible_palindrome)
            if self.isPalindrome(possible_palindrome):
                new_combination = combination + [possible_palindrome]
                self.f(partition, new_combination)
            
    
    def partition(self, A):
        self.A = A
        self.combinations = []
        
        self.f(0, [])
        
        return sorted(self.combinations)
        

        
if __name__=='__main__':
    # print(Solution().isPalindrome("aabaa"))
    # print(Solution().isPalindrome("abba"))
    # print(Solution().isPalindrome("abc"))
    # print(Solution().isPalindrome("ab"))
    print(Solution().partition('aabb'))