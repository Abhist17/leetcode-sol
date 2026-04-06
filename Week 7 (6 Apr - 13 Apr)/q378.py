class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        
        while low < high:
            mid = (low + high) // 2
            
            count = 0
            j = len(matrix) - 1
            
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            
            if count < k:
                low = mid + 1
            else:
                high = mid
        
        return low