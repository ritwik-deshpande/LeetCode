class Solution:
	# @param A : string
	# @return a list of strings
	def f(self, digit, combination):
	    if digit == len(self.A):
	        self.combinations.append(combination)
	        return 
	    
	    for value in self.numbers[int(self.A[digit])]:
	        new_combination = combination + value
	        self.f(digit + 1, new_combination)
	        
	        
	
	
	def letterCombinations(self, A):
	    self.combinations = []
	    self.A = A
	    self.numbers = [['0'], ['1'], ['a','b','c'],['d','e','f'],\
	    ['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r''s'],['t','u''v'],['w','x','y','z']]
	    
	    self.f(0, '')
	    print(sorted(self.combinations))
        
if __name__=='__main__':
    Solution().letterCombinations('23')