class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        
        
        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')
        h1 = len(sentence1) - 1
        h2 = len(sentence2) - 1
        L1 = h1 + 1
        L2 = h2 + 1
        l1 = 0
        l2 = 0
        
        while h1 >= 0 and h2 >= 0:
            if sentence1[h1] == sentence2[h2]:
                h1 -= 1
                h2 -= 1
            else:
                break
                
        while l1 < L1 and l2 < L2:
            if sentence1[l1] == sentence2[l2]:
                l1 += 1
                l2 += 1
            else:
                break
            
        print(l1, h1, l2, h2)
             
        return l1 > h1 or l2 > h2
            