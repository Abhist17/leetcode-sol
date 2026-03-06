class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = energy[:]          
        ans = -10**18
        
        for i in range(n-1, -1, -1):
            if i + k < n:
                dp[i] += dp[i + k]
            ans = max(ans, dp[i])
        
        return ans