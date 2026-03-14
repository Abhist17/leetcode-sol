class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        import math

        def can_finish(time):
            total = 0
            for w in workerTimes:
                # solve x(x+1)/2 * w <= time
                val = (2 * time) // w
                x = int((math.sqrt(1 + 4 * val) - 1) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False

        left = 0
        right = 10**18

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left