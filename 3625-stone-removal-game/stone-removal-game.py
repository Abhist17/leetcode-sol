class Solution:
    def canAliceWin(self, n: int) -> bool:
        k = 10 
        alice = True

        while n >= k:
            n -= k 
            k -= 1
            alice = not alice

        return not alice
