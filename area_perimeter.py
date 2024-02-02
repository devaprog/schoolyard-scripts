import math

def calculate_area_and_perimeter(shape):

 if shape == "rectangle":
   length = float(input("Enter the length of the rectangle: "))
   breadth = float(input("Enter the breadth of the rectangle: "))
   area = length * breadth
   perimeter = 2 * (length + breadth)

 elif shape == "square":
   side = float(input("Enter the side of the square: "))
   area = side * side
   perimeter = 4 * side

 elif shape == "triangle":
   base = float(input("Enter the base of the triangle: "))
   height = float(input("Enter the height of the triangle: "))
   area = 0.5 * base * height
   side1 = float(input("Enter the length of side 1 of the triangle: "))
   side2 = float(input("Enter the length of side 2 of the triangle: "))
   perimeter = base + side1 + side2

 elif shape == "circle":
   radius = float(input("Enter the radius of the circle: "))
   area = math.pi * radius * radius
   perimeter = 2 * math.pi * radius

 elif shape == "regular polygon":
   num_sides = int(input("Enter the number of sides of the regular polygon: "))
   side_length = float(input("Enter the length of a side: "))
   area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
   perimeter = num_sides * side_length

 else:
   print("Invalid shape. Please choose from rectangle, square, triangle, circle, or regular polygon.")
   return

 print("Area:", area)
 print("Perimeter/Circumference:", perimeter)

while True:
 shape = input("Enter the shape (rectangle, square, triangle, circle, regular polygon) or 'q' to quit: ")
 if shape.lower() == 'q':
   break
 calculate_area_and_perimeter(shape.lower())
