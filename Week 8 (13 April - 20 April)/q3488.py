
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = []
        
        for q in queries:
            val = nums[q]
            arr = pos[val]
            
            if len(arr) == 1:
                ans.append(-1)
                continue
            
            i = bisect.bisect_left(arr, q)
           
            left = arr[i - 1] if i > 0 else arr[-1]
            right = arr[i + 1] if i < len(arr) - 1 else arr[0]
           
            def dist(a, b):
                return min(abs(a - b), n - abs(a - b))
            
            ans.append(min(dist(q, left), dist(q, right)))
        
        return ans