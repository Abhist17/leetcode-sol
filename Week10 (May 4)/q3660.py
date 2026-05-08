class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        ans = [0] * n

        start = 0
        currMax = nums[0]

        for i in range(n - 1):
            currMax = max(currMax, nums[i])

            if currMax < suffixMin[i + 1]:
                compMax = max(nums[start:i + 1])

                for j in range(start, i + 1):
                    ans[j] = compMax

                start = i + 1
                currMax = nums[start]

        compMax = max(nums[start:])

        for j in range(start, n):
            ans[j] = compMax

        return ans