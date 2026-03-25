class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
     
        total = sum(sum(row) for row in grid)
      
        if total % 2 != 0:
            return False
        
        half = total // 2
        
        curr = 0
        for i in range(m - 1):  
            curr += sum(grid[i])
            if curr == half:
                return True
        
        col_sum = [0] * n
        for j in range(n):
            for i in range(m):
                col_sum[j] += grid[i][j]
        
        curr = 0
        for j in range(n - 1):
            curr += col_sum[j]
            if curr == half:
                return True
        
        return False