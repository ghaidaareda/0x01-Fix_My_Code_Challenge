#!/usr/bin/python3
""" module for class square """


class Square():
    """ Square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """init method of class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the my square """
        return self.width * self.height

    def Permiter_Of_my_Square(self):
        """perimeter of my square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ str representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ create object"""
    s = square(width=12, height=19)
    print(s)
    print(s.area_of_my_square())
    print(s.Permiter_Of_my_Square())
