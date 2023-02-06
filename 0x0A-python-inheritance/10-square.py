#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
        """A representation of a square"""
            def _init_(self, size):
                        """instantiation of the square"""
                                self.integer_validator("size", size)
                                        self.__size = size
                                                super()._init_(size, size)

                                                    def area(self):
                                                                """"returns the area of the square"""
                                                                        return self.__size ** 2
