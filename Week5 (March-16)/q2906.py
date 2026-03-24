class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        arr = []
        for row in grid:
            arr.extend(row)
        
        k = len(arr)
        res = [1] * k
        
        prefix = 1
        for i in range(k):
            res[i] = prefix
            prefix = (prefix * arr[i]) % MOD
        
        suffix = 1
        for i in range(k - 1, -1, -1):
            res[i] = (res[i] * suffix) % MOD
            suffix = (suffix * arr[i]) % MOD
        
        ans = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(res[idx])
                idx += 1
            ans.append(row)
        
        return ans