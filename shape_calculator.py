class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        output = ''
        if self.width > 50 or self.height > 50:
            output = 'Too big for picture.'
        else:
            output = ''.join(['*' * self.width + '\n' for x in range(self.height)])
        return output
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def __str__(self):
        return f'Square(side={self.width})'
    def set_side(self, new_side):
        super().set_width(new_side)
        super().set_height(new_side)
    def set_width(self, new_width):
        super().set_width(new_width)
        super().set_height(new_width)
    def set_height(self, new_height):
        super().set_width(new_height)
        super().set_height(new_height)
