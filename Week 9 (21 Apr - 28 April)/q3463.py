from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # convert to 1D perimeter positions
        pos = []
        for x, y in points:
            if y == 0:
                pos.append(x)
            elif x == side:
                pos.append(side + y)
            elif y == side:
                pos.append(3 * side - x)
            else:
                pos.append(4 * side - y)

        pos.sort()
        n = len(pos)

        pos = pos + [p + 4 * side for p in pos]

        def can(d):
            for i in range(n):
                count = 1
                last = pos[i]
                for j in range(i + 1, i + n):
                    if pos[j] - last >= d:
                        count += 1
                        last = pos[j]
                        if count == k:
                            return True
            return False

      
        left, right = 0, 4 * side
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans