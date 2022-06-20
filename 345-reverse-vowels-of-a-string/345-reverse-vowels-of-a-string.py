class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = list(s)
        
        vowels = list(filter(lambda x: x in ['a','e','i','o','u'] or x.lower() in ['a','e','i','o','u'], s))
        
        vowels = vowels[::-1]
        
        j = 0
        for i, ch in enumerate(ans):
            if ch in ['a','e','i','o','u'] or ch.lower() in ['a','e','i','o','u'] :
                ans[i] = vowels[j]
                j += 1
                
        return ''.join(ans)