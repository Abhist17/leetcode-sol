class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0

        for d in str(n):
            if d != '0':
                x = x * 10 + int(d)
                digit_sum += int(d)

        return x * digit_sum