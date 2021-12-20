#!/bin/python3

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self._material = "paper"
        
        
class Square:
    def __init__(self):
        self.__height = 2
        self.__width = 2
        
    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side
        
    def get_height(self):
        return self.__height
    
    def set_height(self, h):
        if h >= 0:
            self.__height = h
        else:
            raise Exception('value cannot be less than 0')
        
    
square1 = Square()

print(square1.get_height())    