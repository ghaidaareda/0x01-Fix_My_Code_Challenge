#!/usr/bin/python3
""" Module for class square """


class Square():
    """ Square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Init method of class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the my square """
        return self.width * self.height

    def permiter_Of_my_square(self):
        """Perimeter of my square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Str representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create object"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_Of_my_square())
