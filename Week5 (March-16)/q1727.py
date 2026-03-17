class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        for row in matrix:
           
            row.sort(reverse=True)
            
            for j in range(n):
                height = row[j]
                width = j + 1
                max_area = max(max_area, height * width)
        
        return max_area