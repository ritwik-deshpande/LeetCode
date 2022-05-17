class Solution:
    
    def f(self, n):
        
        if n in self.dp:
            return self.dp[n]
        
        if n == len(self.books):
            return 0
        
        shelf_h = 0
        shelf_w = 0
        min_h_overall = sys.maxsize
        for i in range(n, len(self.books)):
            book = self.books[i]
            shelf_h = max(shelf_h, book[1])
            shelf_w = shelf_w + book[0]

            if shelf_w > self.max_width:
                break
                
            retval = self.f(i + 1)
            min_h_overall = min(min_h_overall, shelf_h + retval)
            
        self.dp[n] = min_h_overall
        return min_h_overall
        
        
    
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        self.books = books
        self.max_width = shelfWidth
        self.dp = {}
        
        return self.f(0)
        