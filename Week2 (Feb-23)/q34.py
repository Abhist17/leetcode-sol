class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target):
            lo, hi, idx = 0, len(nums) - 1, -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    idx = mid
                    hi = mid - 1      # keep searching left
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return idx

        def find_right(nums, target):
            lo, hi, idx = 0, len(nums) - 1, -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    idx = mid
                    lo = mid + 1      # keep searching right
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return idx

        return [find_left(nums, target), find_right(nums, target)]