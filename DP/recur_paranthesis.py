class Solution:
	# @param A : integer
	# @return a list of strings
    def f(self, open_p, close_p, combination):
        if close_p > open_p :
            return
        
        if open_p > self.A :
            return
        
        if open_p == close_p and open_p == self.A:
            self.combinations.append(combination)
            
        new_combination = combination + '('
        self.f(open_p + 1, close_p, new_combination)
        
        another_new_combination = combination + ')'
        self.f(open_p, close_p + 1, another_new_combination)
        return 
    
	def generateParenthesis(self, A):
        self.combinations = []
	    self.A = A

        self.f(0, 0, '')
        # print(self.combinations)
	    return self.combinations

if __name__=='__main__':
    # print(Solution().isPalindrome("aabaa"))
    # print(Solution().isPalindrome("abba"))
    # print(Solution().isPalindrome("abc"))
    # print(Solution().isPalindrome("ab"))
    print(Solution().generateParenthesis(3))