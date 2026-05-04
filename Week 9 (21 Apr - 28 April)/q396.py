class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        current_f = sum(i * val for i, val in enumerate(nums))
        max_f = current_f
        for i in range(n - 1, 0, -1):
            current_f = current_f + total_sum - n * nums[i]
            max_f = max(max_f, current_f)
            
        return max_f