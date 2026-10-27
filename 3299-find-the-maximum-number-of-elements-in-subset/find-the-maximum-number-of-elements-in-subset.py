from collections import Counter

from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)

        ans = 0

        for x in count:
            if x == 1:
                ans = max(ans, count[x] if count[x] % 2 else count[x] - 1)
                continue
            length = 0

            y = x

            while count[y] >= 2:
                length += 2
                y *= y

                if y not in count:
                    break
            if y in count:
                length += 1
            else:
                length -= 1
            
            ans = max(ans, length)
        return ans
        