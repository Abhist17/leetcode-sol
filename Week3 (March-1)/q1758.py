class Solution:
    def minOperations(self, s: str) -> int:
        flip0 = 0
        flip1 = 0

        for i in range(len(s)):
            expec0 = '0' if i % 2 == 0 else '1'
            expec1 = '1' if i % 2 == 0 else '0'
            if s[i] != expec0:
                flip0 += 1
            if s[i] != expec1:
                flip1 += 1
        

        return min(flip0, flip1)
        