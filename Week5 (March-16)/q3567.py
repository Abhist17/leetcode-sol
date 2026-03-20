from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*(n-k+1) for _ in range(m-k+1)]
        
        for i in range(m-k+1):
            for j in range(n-k+1):
                arr = []
                for x in range(i, i+k):
                    for y in range(j, j+k):
                        arr.append(grid[x][y])
                
                arr.sort()
                mn = float('inf')
                
                for t in range(1, len(arr)):
                    if arr[t] != arr[t-1]:
                        mn = min(mn, arr[t] - arr[t-1])
                
                ans[i][j] = 0 if mn == float('inf') else mn
        
        return ans