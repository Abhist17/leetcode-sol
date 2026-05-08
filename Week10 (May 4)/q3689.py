from collections import deque, defaultdict
from math import isqrt

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        mx = max(nums)
        spf = list(range(mx + 1))

        for i in range(2, isqrt(mx) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x):
            return x > 1 and spf[x] == x

        bucket = defaultdict(list)

        for i, val in enumerate(nums):

            x = val
            factors = set()

            while x > 1:
                p = spf[x]
                factors.add(p)

                while x % p == 0:
                    x //= p

            for p in factors:
                bucket[p].append(i)

        q = deque([0])

        vis = [False] * n
        vis[0] = True

        steps = 0

        while q:

            for _ in range(len(q)):

                i = q.popleft()

                if i == n - 1:
                    return steps

                if i - 1 >= 0 and not vis[i - 1]:
                    vis[i - 1] = True
                    q.append(i - 1)

                if i + 1 < n and not vis[i + 1]:
                    vis[i + 1] = True
                    q.append(i + 1)

                if is_prime(nums[i]):

                    p = nums[i]

                    for nxt in bucket[p]:

                        if not vis[nxt]:
                            vis[nxt] = True
                            q.append(nxt)

                    bucket[p].clear()

            steps += 1

        return -1