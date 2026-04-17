class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        
        for t in range(1, target + 1):
            k = t.bit_length()  
            
          
            if (1 << k) - 1 == t:
                dp[t] = k
                continue
        
            dp[t] = k + 1 + dp[(1 << k) - 1 - t]
   
            for j in range(k - 1):
                dp[t] = min(
                    dp[t],
                    (k - 1) + 1 + j + 1 + dp[t - ((1 << (k - 1)) - 1) + ((1 << j) - 1)]
                )
        
        return dp[target]