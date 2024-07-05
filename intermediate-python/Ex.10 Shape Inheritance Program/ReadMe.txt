Features:


This program grants the user with methods to manipulate, set, and return circles and triangles with certain dimensions. This program features the advanced topics of the Python class / object paradigm including dependencies, inheritance, instance variables, getters, setters, __str__, __init__, docstrings, module naming conventions, and general Python syntax. 


In this program, the __str__() method overrides the __str__() method of the object class. Both methods have
the same header definition, but they have different implementations. So, it is polymorphism, and when you change the implementation, that is overriding. This is not to be confused with overloading, which we do not do here, which is defining multiple methods in the same scope with the same name but different parameters (number, types, or both).



Usage:

To use this program, run the "test.py" file, and observe in the "demo.txt" file the results of the print statements from the "test.py" file to observe the method functionality. Also, feel free to re-run the test.py file with your own values -- below are the methods for each Class.


GeometricShape Methods         Description
------------------------------------------------------------------------------------
__init__(opacity, color)       Initializes a new geometric shape with opacity and color.
set_opacity(opacity)           Sets the opacity of the shape.
get_opacity()                  Returns the opacity of the shape.
set_color(color)               Sets the color of the shape.
get_color()                    Returns the color of the shape.


Circle Methods                Description
------------------------------------------------------------------------------------
__init__(opacity, color, radius) Initializes a circle with given opacity, color, and radius.
set_radius(radius)            Sets the radius of the circle.
get_radius()                  Returns the radius of the circle.
get_area()                    Returns the area of the circle.
__str__()                     Returns a string representation of the circle.


Triangle Methods              Description
------------------------------------------------------------------------------------
__init__(opacity, color, base, height) Initializes a triangle with given opacity, color, base, and height.
set_base(base)                Sets the base of the triangle.
get_base()                    Returns the base of the triangle.
set_height(height)            Sets the height of the triangle.
get_height()                  Returns the height of the triangle.
get_area()                    Returns the area of the triangle.
__str__()                     Returns a string representation of the triangle.






Example:

(See the test.py file, and the demo.txt file includes the results of the test.py file)
