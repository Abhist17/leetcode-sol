from typing import List
from collections import defaultdict
import bisect

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
      
        parent = list(range(c + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        for u, v in connections:
            union(u, v)
        
        comp = defaultdict(list)
        for i in range(1, c + 1):
            root = find(i)
            comp[root].append(i)
       
        for root in comp:
            comp[root].sort()
        
        active = [True] * (c + 1)
    
        comp_active = {}
        for root in comp:
            comp_active[root] = comp[root][:]  
        
        ans = []
        
        for t, x in queries:
            root = find(x)
            
            if t == 1:
                if active[x]:
                    ans.append(x)
                else:
                    if comp_active[root]:
                        ans.append(comp_active[root][0])
                    else:
                        ans.append(-1)
            
            else:  
                if active[x]:
                    active[x] = False
                    
                    lst = comp_active[root]
                    idx = bisect.bisect_left(lst, x)
                    if idx < len(lst) and lst[idx] == x:
                        lst.pop(idx)
        
        return ans