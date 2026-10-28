from typing import List
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                x = grid[i][j]

                if i == 0 and j == 0:
                    dp[j] = {x}
                else:
                    prev = set()

                    if i > 0:
                        prev |= dp[j]
                    if j > 0:
                        prev |= dp[j - 1]

                    dp[j] = {v ^ x for v in prev}

        return min(dp[-1])