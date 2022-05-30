class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        op = dividend/divisor
        if op < 0:
            op = math.ceil(op)

        else:
            op = math.floor(op)
        
        if op > 2**31 - 1:
            op = 2**31 - 1
            
        if op < -1*(2**31):
            op = -1*(2**31)
        
        return op