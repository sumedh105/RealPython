class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

rect = Rectangle(5, 4);
print(f"The area of rectangle is: {rect.area()}")

sqr = Square(4)
print(f"The area of square is: {sqr.area()}")
   
sqr.width = 5
print(f"The area of square is: {sqr.area()}")
