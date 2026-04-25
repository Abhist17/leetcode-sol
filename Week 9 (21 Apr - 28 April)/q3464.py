from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)

        # Precompute Manhattan distances
        dist = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dist[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        def can(d):
            chosen = []

            def backtrack(start):
                if len(chosen) == k:
                    return True
                
                for i in range(start, n):
                    ok = True
                    for c in chosen:
                        if dist[i][c] < d:
                            ok = False
                            break
                    
                    if ok:
                        chosen.append(i)
                        if backtrack(i + 1):
                            return True
                        chosen.pop()
                
                return False

            return backtrack(0)

        left, right = 0, 2 * side
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans