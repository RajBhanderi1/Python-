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




#Temp Converter
temp = float(input("Enter temperature : "))
unit = input("Enter unit (C or F) : ")

if unit == "C" :
    temp = round((9/5)*temp + 32 ,1)
    print(f"Temp in F : {temp} °F")

elif unit == "F" :
    temp = round((5/9)*(temp - 32), 1)
    print(f"Temp in C : {temp}°C")

else :
    print("enter F or C only")


#validate user input

# Name should be 12 characters long
# No spaces
# No  digits

name = input("Enter name :")

if len(name) != 12 :
        print("Name should be of 12 characters long only")
elif " " in name or not name.isalpha() :
        print("Name should not contain spaces or digits")




#Compoummd interest Calculator


principle = float(input("Enter principle amount : "))

while principle<=0 :
    print("Principle amount should be greater than 0")
    principle = float(input("Enter principle amount again : "))

rate = float(input("Enter interest rate in % eg: 5 : "))

while rate<=0  :
    print("Interest rate should be greater than 0")
    rate = float(input("Enter interest rate in % eg: 5 again: "))

time = float(input("Enter loan duration in years : "))

while time<=0 :
    print("Loan duration should be greater than 0")
    time = float(input("Enter loan duration in years again : "))  


#assuming yearly compounding

#final_amt_paid

A = principle * (1 + rate/100)** time 

print(f"Final amount paid : {A:,.2f}")