class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))

        visited = set()
        stack = [1]
        ans = float('inf')

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for nei, dist in graph[node]:
                ans = min(ans, dist)

                if nei not in visited:
                    stack.append(nei)

        return ans