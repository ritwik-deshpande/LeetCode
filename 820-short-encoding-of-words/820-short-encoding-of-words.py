class Trie:
    def __init__(self):
        self.children = [None]*26
        self.eow = False
        

class Solution:
    
            
        
    
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        
        words = sorted(words, key = lambda x: len(x), reverse=True)
        
        root = Trie()
        ans = 0
        
        for word in words:
            pointer = root
            word = word[::-1]
            
            is_present = True
            
            for ch in word:
                ch_idx = ord(ch) - ord('a')
                if pointer.children[ch_idx] is None:
                    pointer.children[ch_idx] = Trie()
                    is_present = False
                    
                pointer = pointer.children[ch_idx]
                    
            if not is_present:
                ans = ans + len(word) + 1   
            
            
        return ans
                    
                
            