class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0
        
        for j in range(len(s)):
            
            if i < len(g) and s[j] >= g[i]:
                i += 1
        
        return i