""""
Author: Jack Cacela
File: shapes.py
Defines a class for a general shape named GeometricShape, and two other classes, Circle and Triangle, that inherit from GeometricShape. This is a highly efficient example by using inheritance so we don't have to write the same methods for each additional shape class.
"""


import math

class GeometricShape(object):
    """This class represents a nonspecific shape with general characteristics that can be inherited by another shape class. We can use these methods within the Circle and Triangle classes below even though the methods are defined in this class."""

    def __init__(self, opacity, color):
        self._opacity = opacity
        self._color = color

    def set_opacity(self, opacity):
        """Sets the opacity of the shape."""
        self._opacity = opacity

    def get_opacity(self):
        """Returns the opacity of the shape."""
        return self._opacity

    def set_color(self, color):
        """Sets the color of the shape."""
        self._color = color

    def get_color(self):
        """Gets the color of the shape."""
        return self._color


class Circle(GeometricShape):
    """This class represents a circle shape, and this shape inherits the methods from the GeometricShape class."""

    def __init__(self, opacity, color, radius):
        GeometricShape.__init__(self, opacity, color)  # Initialize the circle with GeometricShape's init method, along with GeometricShape's instance variables that can be used in the Circle class due to inheritance.
        self._radius = radius

    def set_radius(self, radius):
        """Sets the radius of the circle."""
        self._radius = radius

    def get_radius(self):
        """Gets the radius of the circle."""
        return self._radius

    def get_area(self):
        """Gets the area of the circle."""
        return math.pi * self._radius ** 2

    def __str__(self):
        # Using getter methods for attributes with single underscores (like _color, _opacity, _base, _height, etc.)
        # is a good practice to promote encapsulation and maintainability.
        return "color: " + str(self.get_color()) + "\n" + \
               "opacity: " + str(self.get_opacity()) + "\n" + \
               "radius: " + str(self._radius)


class Triangle(GeometricShape):
    """This class represents a triangle shape, and this shape inherits the methods from the GeometricShape class."""

    def __init__(self, opacity, color, base, height):
        GeometricShape.__init__(self, opacity, color)
        self._base = base
        self._height = height

    def set_base(self, base):
        """Sets the base of the triangle."""
        self._base = base

    def get_base(self):
        """Returns the base of the triangle."""
        return self._base

    def set_height(self, height):
        """Sets the height of the triangle."""
        self._height = height

    def get_height(self):
        """Gets the height of the triangle."""
        return self._height

    def get_area(self):
        """Gets the area of the triangle."""
        return self._base * self._height / 2

    def __str__(self):
        # Using getter methods for attributes with single underscores (like _color, _opacity, _base, _height, etc.)
        # is a good practice to promote encapsulation and maintainability.
        return "color: " + str(self.get_color()) + "\n" + \
               "opacity: " + str(self.get_opacity()) + "\n" + \
               "base: " + str(self._base) + "\n" + \
               "height: " + str(self._height)