"""
Program: Sphere
Author: Jack Cacela

This program calculates the diameter,
circumference, surface area, and volume of a sphere.

Input: The radius of the sphere
Output: The diameter, circumference, surface area, 
and volume of the sphere.
"""

from math import pi

# Get the radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# Calculate the four characteristics of the sphere
diameter = round((2 * radius), 2)
circumference = round((diameter * pi), 2)
surface_area = round((4)*(pi)*(radius**2), 2)
volume = round((4/3) * (pi) * (radius**3), 2)

# Return the results
print("Diameter = ", diameter)
print("Circumference = ", circumference)
print("Surface_area = ", surface_area)
print("Volume = ", volume)