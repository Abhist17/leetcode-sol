class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                val = candidates[i]

                if val > remaining:
                    break  # strong pruning

                path.append(val)
                dfs(i, remaining - val)  # reuse same index
                path.pop()

        dfs(0, target)
        return res

        
    