from bisect import bisect_right
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        
        ans = [-1] * n
        last_rain = {}      
        dry_days = []             
        for i in range(n):
            if rains[i] == 0:
                dry_days.append(i)
                ans[i] = 1                   
            else:
                lake = rains[i]
                
                if lake in last_rain:
                    last = last_rain[lake]
                    
                    index = bisect_right(dry_days, last)
                    
                    if index == len(dry_days):
                        return []
                    
                    dry_day = dry_days[index]
                    ans[dry_day] = lake
                    
                    dry_days.pop(index)
                
                last_rain[lake] = i
        
        return ans