class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.eow = False
        
    

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
        

    def addWord(self, word: str) -> None:
        
        ptr = self.root
        for letter in word:
            
            idx = ord(letter) - ord('a')
            
            if not ptr.children[idx]:
                ptr.children[idx] = TrieNode()
                
                
            ptr = ptr.children[idx]
                
        
        ptr.eow = True
            
      
    def searchUtil(self, arr_idx, word, ptr):
        
        if arr_idx == len(word):
            return ptr.eow
        
        letter = word[arr_idx]
        # print(letter)
        
        if letter == '.':
            alpha_indexes = range(0, 26)
            for alpha_index in alpha_indexes:
                if ptr.children[alpha_index] and  self.searchUtil(arr_idx + 1, word, ptr.children[alpha_index]):
                    return True
                
            return False
                
                
        else:
            alpha_index = ord(letter) - ord('a')

            
        
            return ptr.children[alpha_index] and self.searchUtil(arr_idx + 1, word, ptr.children[alpha_index])

    def search(self, word: str) -> bool:
        
        ptr = self.root
            
        return self.searchUtil(0, word, ptr)