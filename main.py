import math
import time
import random

#print("Hello world")
#p# Variables

# first_name = "John"
# last_name = "Doe"
#print(first_name)
#print("hello " , first_name , " bye" )
#print(f"hello {first_name} {last_name} ")

#age = 10
#print(f"your age : {age}")

# is_student = False

# if is_student:
#     print("you are a student")
# else: 
#     print("you are not a student")

#Typecasting

# str()
# int()
# float()
# bool()

# name= "John"
# age = 10
# gpa = 3.5
# is_student = True

# print(type(name))
# print(type(age))    
# print(type(gpa))
# print(type(is_student))

# age = float(age)
# gpa = int(gpa)

# name = bool(name)
# print(name)



# Input

# name = input("Enter your name :")
# age = int(input("Enter your age here:"))
# age = age + 1

# print (f"Name: {name}, age : {age}")


#Arithmetic operations


# age = 1

# age += 2
# print(age)
# # age **= 4
# # age -= age

# remainder = age % 5

# print(remainder)
# remainder =float(remainder)

# print(remainder)


# x = 1.9
# y = -3
# z = x * y

# result = round(x)
# print(result)

# #print(f"{math.pi}\n {math.e}{math.sqrt(16)} {math.pow(2,3)}")



#if /else

# age = int(input("Enter your age : "))

# if age>18 :
#     print("An adult")
# elif age>20 and age<30 :
#     print("You are in your twenties")
# else:
#    print(" not an adult")


# or and not


# temp = 60
# is_sunny = False


# if temp>= 50 and is_sunny :
#     print("It is sunny and hot")

# elif temp>= 50 and not is_sunny :
#     print("It is sunny and cloudy")
# else:
#     print("It is cold")


#ternary operators

# num = 310
# print("Even" if num % 2 == 0 else "Odd")

# str = input("Enter string :")

# print(f"Length of str : {len(str)}")

# X = input("Enter character to find :")
# print(f"Position of {X} : {str.find(X)}")
# Y = input("Enter character to find from last:")
# print(f"Position of {Y} : {str.rfind(Y)}")
# print(f"Capitalized string: {str.capitalize()}")
# print(f"Uppercase string: {str.upper()}")
# print(f"Lowercase string: {str.lower()}")       
# print(f"All Digits>? :{str.isdigit()}")


# print(help(str))

# str ="1234-5678-9012-3456"

# # print(str[0:4])
# print(str[::-1])


# num1 = 12000000.21315
# num2 = -160000.020
# num3  = 12156516

# print(f"Num1 :{num1:+,.2f}")
# print(f"Num2 :{num2:+,}")
# print(f"Num3 :{num3:+,}")

# name = input("enter name:")

# while name == " " or name == "" :
#     print("Name cannot be empty")
#     name = input("enter name again :")
    
# print(f"Name : {name}")


# for x in range (1,11) :
#     print (x)
    
# print("hello")
    
    
# for x in reversed(range(1,12,2)) :
#     print (x)

#   =("apple", "banana", "cherry", "date", "elderberry")
# print(fruits)
# # fruits.append("hello")
# print(fruits)
# fruits.insert(1,"hi")
# print(fruits)
# fruits.remove(fruits[1])
# print(fruits)
# fruits.sort()
# fruits.reverse()
# fruits.pop("apple")
# print(fruits)


# fruits =["apple", "banana", "cherry", "date", "elderberry"]
# meat = ["egg","fish","chicken"]
# flower = ["rose","sunflower"]

# groceries = [fruits,meat , flower]


# # print(groceries[0][1])

# for x in groceries:
#     # for y in x:
#     # print(x)
#     for y in x:  
#         print(y,end=" ")
#     print()
    

# capitals = {"USA" : "DC",
#             "INDIA" :"NEW DEHLI",
#             "CHINA" : "BEIGINJ"}

# capitals.update({"GERMANY": "BERLIN"})
# print(capitals)
# capitals.update({"INDIA" : "dehli"})
# print(capitals)
# capitals.pop("INDIA")
# print(capitals)
# capitals.popitem()
# print(capitals)
# print(capitals.keys())

# print(capitals.values())
# capitals.clear()

# print(capitals)


# opt =["ROCK", "PAPER", "SCISSORS"]



# num = random.shuffle(opt)
# print(opt)

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

