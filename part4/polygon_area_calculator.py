
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return (self.width + self.height)*2
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        string = ''
        if self.width >50 or self.height>50:
            return 'Too big for picture.'
        for _ in range(self.height):
            string += ('*'*self.width + '\n')
        return string

    def get_amount_inside(self, rectangle):
        return self.get_area()//rectangle.get_area()

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return f'Square(side={getattr(self, "height")})'

    def set_side(self, side):
        self.width, self.height = side, side
    
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

rectangle = Rectangle(3,6)
print(rectangle.get_area())
print(rectangle.get_perimeter())
print(rectangle.get_diagonal())
print(rectangle.get_picture())
print(rectangle)
square = Square(2)
square.set_side(3)
print(square.get_area())
square.set_width(4)
print(square)