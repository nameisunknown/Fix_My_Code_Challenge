#!/usr/bin/python3
"""This module contains the Square class"""


class Square():
    """This class represents a square"""

    def __init__(self, width, height):
        
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the square"""

        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the value of the width"""

        if type(value) is not int:
            raise TypeError ("width muse be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the square"""

        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the value of the height"""

        if type(value) is not int:
            raise TypeError ("height muse be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area_of_my_square(self):
        """Area of the square"""

        return self.width * self.height

    def PerimeterOfMySquare(self):
        """Returns the perimeter of the square"""

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns the string representaion of the square"""

        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
