from collections import Counter
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        values = sorted(freq.keys())
        
        n = len(values)
        dp = [0] * n
        
        for i in range(n):
            total = values[i] * freq[values[i]]
            
            j = i - 1
            while j >= 0 and values[i] - values[j] <= 2:
                j -= 1
            
            take = total + (dp[j] if j >= 0 else 0)
            skip = dp[i-1] if i > 0 else 0
            
            dp[i] = max(take, skip)
        
        return dp[-1]
        