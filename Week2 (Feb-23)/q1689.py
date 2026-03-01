class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        
        for ch in n:
            max_digit = max(max_digit, int(ch))
            
            if max_digit == 9:
                return 9
        
        return max_digit