# Name:
#
# Date:
#
# Period:
#
# Description:  Define the functions described in comments below.
#               Functions should should pass all tests.  Proper
#               pep-8 formatting should be used and comments should
#               be added or updated where appropriate
#
import math

# rect_area returns the area of a rectangle with a given length and width
# It takes 2 params, the length and width of the rectangle
def rect_area(length, width):


    return 0

# rect_perimeter returns the perimeter of a rectangle with a given length and width
# It takes 2 params, the length and width of the rectangle
def rect_perimeter(length, width):


    return 0

# triangle_area returns the area of a triangle with a given base and height
# it takes two parameters (base and height) that represents the base and height of the triangle
def triangle_area(base, height):


    return 0

# circle_area returns the area of a circle with a given radius
# it takes one parameter (radius) that represents the radius of the circle
def circle_area(radius):


    return 0

# circle_perimeter returns the perimeter of a circle with a given radius
# it takes one parameter (radius) that represents the radius of the circle
def circle_circumference(radius):


    return 0


# calculate_slope returns the slope between the 2 points (x1, y1) and (x2, y2)
# it takes in 4 params, x1 and y1 that represent the x and y coordinates of point 1
# and x2 and y2 that represent the x and y coordinates of point 2
def calculate_slope(x1, y1, x2, y2):


    return 0


def main():
    print("A rectangle with sides 10 and 5 have a perimeter of:", rect_perimeter(10,5))
    print("A rectangle with sides 10 and 5 have an area of:", rect_area(10,5))
    print("A triangle with base 10 and height 5 have an area of:", triangle_area(10,5))
    print("A circle with radius 5 has an area of:", circle_area(5))
    print("A circle with radius 5 has an circumference of:", circle_circumference(5))
    print("The slope of the line between (1,1) and (5,3) is:", calculate_slope(1,1,5,3))


if __name__ == '__main__':
    main()


