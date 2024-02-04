import math

def calculate_volume(shape):
    """Prompts for variables and calculates volume of the given shape."""

    if shape == "cube":
        side = float(input("Enter the side of the cube: "))
        volume = side ** 3

    elif shape == "cuboid":
        length = float(input("Enter the length of the cuboid: "))
        breadth = float(input("Enter the breadth of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        volume = length * breadth * height

    elif shape == "cylinder":
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        volume = math.pi * radius**2 * height

    elif shape == "sphere":
        radius = float(input("Enter the radius of the sphere: "))
        volume = (4 / 3) * math.pi * radius**3

    elif shape == "cone":
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        volume = (1 / 3) * math.pi * radius**2 * height

    elif shape == "pyramid":
        length = float(input("Enter the base length of the pyramid: "))
        breadth = float(input("Enter the base breadth of the pyramid: "))
        height = float(input("Enter the height of the pyramid: "))
        volume = (1 / 3) * length * breadth * height

    else:
        print("Invalid shape. Please choose from cube, cuboid, cylinder, sphere, cone, or pyramid.")
        return

    print("Volume:", volume)

while True:
    shape = input("Enter the shape (cube, cuboid, cylinder, sphere, cone, pyramid) or 'q' to quit: ")
    if shape.lower() == 'q':
        break
    calculate_volume(shape.lower())
