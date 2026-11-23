class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26
        new_children = [[] for _ in range(n)]

        def build(node):
            c = ord(s[node]) - ord('a')
            prev = last[c]

            if prev != -1:
                new_children[prev].append(node)
            elif parent[node] != -1:
                new_children[parent[node]].append(node)

            last[c] = node

            for child in children[node]:
                build(child)

            last[c] = prev

        build(0)

        ans = [0] * n

        def dfs(node):
            size = 1
            for child in new_children[node]:
                size += dfs(child)
            ans[node] = size
            return size

        dfs(0)
        return ans