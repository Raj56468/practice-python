from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
    
print("Area of Circle with radius 5:", circle(5).area())
print("Area of Square with side 4:", square(4).area())