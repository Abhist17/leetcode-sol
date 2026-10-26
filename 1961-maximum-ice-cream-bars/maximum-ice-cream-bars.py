from typing import List
class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count = 0

        for cost in costs:
            if coins < cost:
                break

            coins -= cost
            count += 1

        return count