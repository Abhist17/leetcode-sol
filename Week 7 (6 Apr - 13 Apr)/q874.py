class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0
        x, y = 0, 0
        max_distance = 0
        obstacle_set = set(map(tuple, obstacles))
        
        for command in commands:
            
            if command == -2:
                direction_index = (direction_index - 1) % 4
            
            elif command == -1:
                direction_index = (direction_index + 1) % 4
            
            else:
                dx, dy = directions[direction_index]
                
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    
                    if (next_x, next_y) in obstacle_set:
                        break
                    
                    x, y = next_x, next_y
                    max_distance = max(max_distance, x*x + y*y)
        
        return max_distance