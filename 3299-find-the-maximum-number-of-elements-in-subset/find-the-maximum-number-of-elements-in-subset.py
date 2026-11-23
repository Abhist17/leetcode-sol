class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        for x in cnt:
            if x == 1:
                ans = max(ans, cnt[x] if cnt[x] % 2 else cnt[x] - 1)
                continue

            length = 0
            cur = x

            while cnt[cur] >= 2:
                length += 2
                cur *= cur

            if cnt[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans