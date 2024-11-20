class Rectangle():
    def __init__(self, height, width) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
object = Rectangle(5,20)
print(object)