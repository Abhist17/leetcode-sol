class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        
        max_distance = 0      
        prev_index = -1       
        
        
        for i in range(len(binary)):
            if binary[i] == '1':
                
                if prev_index != -1:
                    distance = i - prev_index
                    max_distance = max(max_distance, distance)
                
                prev_index = i
        
        return max_distance