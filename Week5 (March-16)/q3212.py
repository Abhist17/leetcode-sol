from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ps = [[0]*(m+1) for _ in range(n+1)]
        px = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                v = 1 if grid[i][j] == 'X' else -1 if grid[i][j] == 'Y' else 0
                ps[i+1][j+1] = v + ps[i][j+1] + ps[i+1][j] - ps[i][j]
                px[i+1][j+1] = (grid[i][j] == 'X') + px[i][j+1] + px[i+1][j] - px[i][j]
        
        return sum(
            1
            for i in range(n)
            for j in range(m)
            if ps[i+1][j+1] == 0 and px[i+1][j+1] > 0
        )