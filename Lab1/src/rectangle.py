"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self):
        self.__width = 0
        self.__height = 0 
        # In Python, the concept of "private" variables is not enforced as strictly as it is in languages like Java or C++.
        # Instead, Python uses a convention of name mangling to make it less likely that a subclass will accidentally override 
        # an attribute or method from a superclass. This is achieved by prefixing the variable name with double underscores __.

    @abstractmethod
    def set_values(self, x, y):
        pass

    @abstractmethod
    def area(self):
        pass
    # The abstract methods set_values and area in Shape should not have implementations.
    # They are supposed to be placeholders for subclasses to fill in.

    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def set_width(self, width):
        self.__width = width
    
    def set_height(self, height):
        self.__height = height
    

class Rectangle(Shape):
    def set_values(self, x, y):
        self.set_width = x
        self.set_height = y

    def area(self):
        return self.get_width() * self.get_height()


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
