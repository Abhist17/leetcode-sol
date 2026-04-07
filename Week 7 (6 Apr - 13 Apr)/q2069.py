from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        
        self.dir = 0
        self.dirs = ["East", "North", "West", "South"]
        
        self.perimeter = 2 * (width + height) - 4
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        num %= self.perimeter
        
        while num > 0:
            if self.dir == 0:  
                move = min(num, self.w - 1 - self.x)
                self.x += move
            elif self.dir == 1: 
                move = min(num, self.h - 1 - self.y)
                self.y += move
            elif self.dir == 2:  
                move = min(num, self.x)
                self.x -= move
            else:  
                move = min(num, self.y)
                self.y -= move

            num -= move

            if num > 0:
                self.dir = (self.dir + 1) % 4


        if self.x == 0 and self.y == 0:
            self.dir = 3  

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        
        if not self.moved:
            return "East"
        return self.dirs[self.dir]