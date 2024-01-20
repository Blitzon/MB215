PI = 3.14159 

def calculate_circle_area(radius):
    area = PI * (radius ** 2)
    return area

radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area}")
