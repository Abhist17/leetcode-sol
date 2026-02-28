class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        
        result = 0
        length = 0   # current bit length
        
        for i in range(1, n + 1):
            
            # if i is power of 2, increase bit length
            if (i & (i - 1)) == 0:
                length += 1
            
            # shift result and add i
            result = ((result << length) + i) % MOD
        
        return result