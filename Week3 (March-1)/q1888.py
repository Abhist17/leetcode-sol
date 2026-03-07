class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s * 2
        
        res = float('inf')
        diff1 = diff2 = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] != ('0' if r % 2 == 0 else '1'):
                diff1 += 1
            if s[r] != ('1' if r % 2 == 0 else '0'):
                diff2 += 1
            
            if r - l + 1 > n:
                if s[l] != ('0' if l % 2 == 0 else '1'):
                    diff1 -= 1
                if s[l] != ('1' if l % 2 == 0 else '0'):
                    diff2 -= 1
                l += 1
            
            if r - l + 1 == n:
                res = min(res, diff1, diff2)
        
        return res