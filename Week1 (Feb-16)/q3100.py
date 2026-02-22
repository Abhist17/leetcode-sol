class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty = 0
        exchange = numExchange
        total_drunk = 0

        total_drunk += full_bottles
        empty += full_bottles
        full = 1
    
        while empty >= exchange:
            

            empty -= exchange
            exchange += 1           
            
            total_drunk += 1
            empty += 1  
        
        return total_drunk
        