class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        
      
        for row in grid:
            for val in row:
                arr.append(val)

      
        base = arr[0]        
        for val in arr:
            if (val - base) % x != 0:
                return -1
        
       
        arr = [val // x for val in arr]
        arr.sort()
        
       
        median = arr[len(arr) // 2]
        
        ops = 0
        for val in arr:
            ops += abs(val - median)
        
        return ops