class Rectangle:
    def __init__(self, length:int, width:int) -> None:
        self.length = length
        self.width = width

    def area(self):
        if self.width and self.length: 
            return self.width * self.length
    
class sqaure(Rectangle):
    def __init__(self, side:int):
        self.side = side

    def area(self):
        if self.side:
            return self.side**2
    

rectangle = Rectangle(5,7)
print(rectangle.area())
square = sqaure(10)
print(square.area())