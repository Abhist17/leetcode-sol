from collections import defaultdict, Counter
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in allowedSwaps:
            union(x, y)

        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)

        res = 0

        for indices in groups.values():
            count = Counter(source[i] for i in indices)
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    res += 1

        return res