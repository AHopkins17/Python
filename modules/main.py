from math_operations import calculator
from math_operations import geometry

# Calculator
result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)

# Geometry
rect_area = geometry.area_of_rectangle(10, 5)
print("Area of rectangle:", rect_area)

tri_area = geometry.area_of_triangle(8, 5)
print("Area of triangle:", tri_area)

circ_area = geometry.area_of_circle(7)
print("Area of circle:", circ_area)