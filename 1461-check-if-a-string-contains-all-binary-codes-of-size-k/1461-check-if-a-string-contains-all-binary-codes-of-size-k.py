class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        # for num in range(2**k):
        #     # print(num)
        #     bin_code = bin(num).replace('0b', '').rjust(k, '0')
        #     # print(bin_code)
        #     if bin_code not in s:
        #         return False
        
        comb = []
        for i in range(len(s) - k + 1):
            comb.append(s[i: i + k])
            
        # print(set(comb))
        if len(set(comb)) == 2**k:
            return True
            
        return False
        