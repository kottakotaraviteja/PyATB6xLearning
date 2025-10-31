"""
Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
i/p - int side1 == side2 =side3 → isoceles
o/p = result in string - iso, eq, scalene
"""

def triangle_area(side1,side2,side3):

    if(side1==side2==side3):
        print("Equilateral triangle")
    elif(side1==side2 or side3==side1 or side3==side2):
        print("Isoceles triangle")
    else:
        print("Scalene triangle")

triangle_area(int(input("side1")),int(input("side2")),int(input("side3")))