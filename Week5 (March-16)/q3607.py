from typing import List
from collections import defaultdict
import heapq

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
            comp[find(i)].append(i)
        
        comp_heap = {}
        for root in comp:
            heapq.heapify(comp[root])
            comp_heap[root] = comp[root]
        
        active = [True] * (c + 1)
        ans = []
        
        for t, x in queries:
            root = find(x)
            if t == 1:
                if active[x]:
                    ans.append(x)
                else:
                    heap = comp_heap[root]
                    while heap and not active[heap[0]]:
                        heapq.heappop(heap)
                    ans.append(heap[0] if heap else -1)
            else:
                active[x] = False
        
        return ans