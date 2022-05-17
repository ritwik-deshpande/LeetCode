class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        i = 0
        j = 0
        max_fruits = 0
        limit = 2
        L = len(fruits)
        basket = collections.defaultdict(int)
        number_of_fruits = 0
        
        while i < L:
            if basket[fruits[i]] == 0:
                basket[fruits[i]] = 1
                number_of_fruits = number_of_fruits + 1
            else:
                basket[fruits[i]] += 1
                
            while number_of_fruits > 2 and j < L:
                basket[fruits[j]] -= 1
                if basket[fruits[j]] == 0:
                    number_of_fruits = number_of_fruits - 1
                    
                j = j + 1
            
            # print(i, j, basket, number_of_fruits)
            max_fruits = max(max_fruits, i - j + 1)  
            i = i + 1
            
        return max_fruits
            
        