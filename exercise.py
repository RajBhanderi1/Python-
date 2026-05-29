import math
import time
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


#python timer


my_time = input("Enter time in seconds : ")

while my_time.isdigit() == False :
    print("Invalid input enter numbers only")
    my_time = int(input("Enter time in seconds and digit only again : "))

my_time = int(my_time)

while my_time<=0:
    print("Time should be greater than 0")
    my_time = int(input("Enter time in seconds again : "))


# for S in range(my_time,0,-1) :

#     if S > 3600 :
            
#             H = S // 3600
#             S = S % 3600
#             M = S // 60
#             S = S % 60
#             print(f"Time remaining : {H:02d}:{M:02d}:{S:02d}")
#             time.sleep(1)
#     elif S >60 :
                
#                 M = S // 60
#                 S = S % 60
#                 print(f"Time remaining : 00:{M:02d}:{S:02d}")
#                 time.sleep(1)


#     elif S < 60:
#         print(f"Time remaining : 00:00:{S:02d}")
#         time.sleep(1)
 
for x in range(my_time , 0, -1) :
    s = x % 60
    m = int(x / 60) % 60
    h = int(x / 3600) 
    print (f"Time remaining : {h:02d}:{m:02d}:{s:02d}")   
    time.sleep(1) 
print("Time's up!")


# build a rectangle

rows = int(input("Enter number of rows : "))
col = int(input("Enter number of columns :"))

for x in range (rows) :
    for y in range(col) :
        print("*", end = "")
    
    print()

# food cart problem


foods =[]
prices =[]
total = 0


while True:

    food = input("Enter food item name (enter q to quit):")
    if food == "q" :
        break
    while not food.isalpha():
        food = input("Enter food item name again in alphabets only:")
    price = input(f"Enter price of {food} : ")
    while not price.isdigit() or price == " " or price == "" or price <= "0":
        price = input(f"Enter price of {food} again in digits only and greater than 0 : ")

    foods.append(food)
    prices.append(float(price))

    total += float(price)

print(foods)
print(prices)
print(f"Total price : {total:0.2f}")