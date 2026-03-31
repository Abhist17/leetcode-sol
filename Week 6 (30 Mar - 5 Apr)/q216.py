class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if len(path) == k and target == 0:
                result.append(path)
                return
            for i in range(start, 10):
                if i > target:
                    break
                backtrack(i + 1, path + [i], target - i)

        result = []
        backtrack(1, [], n)
        return result