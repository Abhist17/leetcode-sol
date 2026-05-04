from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index_map = defaultdict(list)

        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        result = [0] * len(nums)

        for indices in index_map.values():
            prefix_sum = [0]
            
            for idx in indices:
                prefix_sum.append(prefix_sum[-1] + idx)
            
            total = prefix_sum[-1]
            n = len(indices)
            
            for k, idx in enumerate(indices):
               
                left = idx * k - prefix_sum[k]
              
                right = (total - prefix_sum[k+1]) - idx * (n - k - 1)
                
                result[idx] = left + right
        
        return result
        