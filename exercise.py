import math


# area calculator
length = float(input("Enter the length : "))
width = float(input("Enter the width  : "))

area = length * width

print (f" Area of rectangle:  {area}")


# # matlibs game

print("Welcome to the matlibs game!")

adjective1 = input("Enter and adjective : ")
noun1 = input("Enter a noun : ")
adjective2 = input("Enter another adjective : ")
adjective3 = input("Enter one more adjective : ")

print(f" Today i went to a {adjective1} zoo")
print(f" The {noun1} was {adjective2} and {adjective3}")


# circumference of circle

radius = float(input("Enter radius of circle : "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f" Circumference of circle : {circumference}")
print(f" Area of circle : {area}")

