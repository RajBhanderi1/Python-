import math
import time
import random

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


# numpad

num_pad = (("1","2","3"),("4","5","6"),("7","8","9"),("#","0","*"))

for x in num_pad :
    for y in x :
        print(y,end= " ")
    print()

# quiz game


questions = (
    ("What is the capital of India?"),
    ("Which planet is known as the Red Planet?"),
    ("What is 5 * 6?"),
    ("Which language is primarily used for AI and Data Science?"),
    ("Who wrote 'Romeo and Juliet'?")
)

options = (
    ("A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"),
    ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
    ("A. 25", "B. 35", "C. 30", "D. 40"),
    ("A. Java", "B. C++", "C. Python", "D. HTML"),
    ("A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. J.K. Rowling")
)

answers = (
    "B",
    "B",
    "C",
    "C",
    "B"
)
guess = []
count = 0

opt = ["A","B","C","D"]
for x in range(len(questions)):
    print(questions[x])
    for y in options[x]:
        print(y, end="\n")
    
    print()
    
    guess_temp= input("enter your guess (A/B/C/D):").upper()

    while True:
        if guess_temp not in opt or guess_temp =="" or guess_temp == "0" :
            guess_temp= input("enter your guess again (A/B/C/D):").upper()
        else :
            break
    print()
    guess.append(guess_temp)

for x in range(5):
     if guess[x] == answers[x]:
        count += 1
    

print(f"Your Answers : {guess}")
print(f"Correct Answers :{answers}")
print(f"Out of which number of correct answers : {count} ")


# Menu cart using dictionaries


menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Sandwich": 90,
    "French Fries": 80,
    "Coke": 40,
    "Coffee": 60,
    "Ice Cream": 70,
    "Biryani": 220,
    "Salad": 100
}
print("MENU :")
for key , value in menu.items():
    
    print(f"{key:<14} : {value: >8.2f}")
cart = []
total = 0

while True :
    
    cart_temp = input("Enter items to add to cart (press Q to quit) : ").title()
    
    if cart_temp== "Q":
        break    
    while cart_temp not in menu or cart_temp=="" or cart_temp == "0" :
            cart_temp = input("Enter items to add to cart again: ").title()
            if cart_temp == "Q":
                break
    if cart_temp == "Q":
        break
    cart.append(cart_temp)    
    
for item in cart:
     
    print(item)
    total += float(menu[item])
    
print(f"Total of cart :{total}")




# num guessing game
low = 0
high = 100
count = 0

num = random.randint(low,high)

guess = input("Enter your guess between 0 to 100(including 0 & 100) :")
while True :
    if guess.isdigit():
        
        while True :
            guess = int(guess)
            if guess < low or guess > high :
                guess = input("Please enter a valid number only in range 0 to 100 : ")
                

            elif guess < num :
                guess = input(f"{guess} is too low, try bigger number again : ")
                count += 1
            
            elif guess > num :
                guess =input(f"{guess} is too big try smaller number again : ")
                count += 1
                

            elif guess == num :
                print("Congrats your guessed number is correct")
                count += 1
                break

            else :
                input("Please enter a valid number only : ")
        


        print(f"You guessed correct number in {count} times")
        break
    else :
        print("Enter digits only")
        guess = input("Enter your guess between 0 to 100(including 0 & 100) :")
