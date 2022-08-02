class Solution(object):
    
    def f(self, needs):
        
        cost = sum(self.price[i]*needs[i] for i in range(self.N))
        
        for sp in self.special:
            
            new_needs = tuple([needs[i] - sp[i] for i in range(self.N)])
            if min(new_needs) >= 0:
                cost = min(cost, self.f(new_needs) + sp[-1])
                
        return cost
            
    
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.N = len(price)
        self.price = price
        self.special = special
        
        return self.f(tuple(needs))
                   
                         
        
        