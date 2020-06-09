#!/usr/bin/python3

"""
Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle child of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
                raise ValueError("y must be >= 0")
        self.__y = y

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
                raise ValueError("x must be >= 0")
        self.__x = x

    def area(self):
        """return area of instance"""
        return self.__width * self.__height

    def display(self):
        """rectangle with '#'"""
        print("\n" * self.__y, end="")
        print(((self.__x * ' ') + ('#' * self.__width +
                                   '\n')) * self.__height, end="")

    def __str__(self):
        """str representative of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update attributes"""
        if args:
            x = 0
            for arg in args:
                if x == 0:
                    self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.height = arg
                elif x == 3:
                    self.x = arg
                elif x == 4:
                    self.y = arg
                x += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of attributes"""
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['width'] = self.__width
        new_dict['height'] = self.__height
        new_dict['x'] = self.__x
        new_dict['y'] = self.__y
        return new_dict
