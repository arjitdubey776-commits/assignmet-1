from geometry.circle import area as circle_area
from geometry.rectangle import area as rectangle_area

radius = float(input("Enter circle radius: "))
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

print("Circle area:", circle_area(radius))
print("Rectangle area:", rectangle_area(length, width))
