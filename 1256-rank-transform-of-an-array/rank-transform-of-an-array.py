class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(set(arr))
        rank = {num: i + 1 for i, num in enumerate(sorted_arr)}

        return [rank[num] for num in arr]