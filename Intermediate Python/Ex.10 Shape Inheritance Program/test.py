from shapes import Circle, Triangle

# Create a circle object and add parameters
circle = Circle(5, "red", 6.0)

# Print the circle
print("Circle after adding these parameters:")
print(circle)  # Calls the __str__ method of Circle on the object

# Get the area of the circle
print("Circle area:", circle.get_area())

# Create a triangle object and add parameters
triangle = Triangle(10, "green", 4.0, 10.0)

# Print the triangle
print("Triangle after adding these parameters:")
print(triangle)  # Calls the __str__ method of Triangle on the object

# Get the area of the triangle
print("Triangle area:", triangle.get_area())

# Wait for user input before exiting
input("Press Enter to exit...")