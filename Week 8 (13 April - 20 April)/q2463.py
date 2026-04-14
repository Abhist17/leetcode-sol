from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n = len(robot)
        INF = float('inf')
        
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for pos, limit in factory:
            new_dp = dp[:]
            
            for i in range(1, n + 1):
                cost = 0
                
                for k in range(1, min(limit, i) + 1):
                    cost += abs(robot[i - k] - pos)
                    new_dp[i] = min(new_dp[i], dp[i - k] + cost)
            
            dp = new_dp
        
        return dp[n]