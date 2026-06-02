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

# dice_art = {
#                 1: """
#             ┌───────┐
#             │       │
#             │   ●   │
#             │       │
#             └───────┘
#             """,

#                 2: """
#             ┌───────┐
#             │ ●     │
#             │       │
#             │     ● │
#             └───────┘
#             """,

#                 3: """
#             ┌───────┐
#             │ ●     │
#             │   ●   │
#             │     ● │
#             └───────┘
#             """,

#                 4: """
#             ┌───────┐
#             │ ●   ● │
#             │       │
#             │ ●   ● │
#             └───────┘
#             """,

#                 5: """
#             ┌───────┐
#             │ ●   ● │
#             │   ●   │
#             │ ●   ● │
#             └───────┘
#             """,

#                 6: """
#             ┌───────┐
#             │ ●   ● │
#             │ ●   ● │
#             │ ●   ● │
#             └───────┘
#             """
# }

# roll = random.randint(1,6)
# # for roll in dice_art:
# print(dice_art[roll])


# def invoice(username,amount = 0 ,date= "20"):
#     print(f"Username: {username} Amount: {amount} Date: {date}")
#     # print(f"Amount: {amount}")
#     # print(f"Date: {date}")


# invoice(amount = 1000,username = "raj",date = 20)

# # def add(x,y):
# #     z = x + y
# #     return z

# x = int(input("Enter x : "))
# y = int(input("Enter y : "))
# print(add(x,y))



# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg,end=" ")
#     print()
#     # for value in kwargs.values() :
#     #     print(value,end=" ")
#     # print()
#     if 'apt' in kwargs.keys() and 'area' in kwargs.keys():
#         print(f"{kwargs.get('area')} {kwargs.get('apt')},")
#     elif 'apt' not in kwargs.keys():
#         print(f"{kwargs.get('area')},")
#     elif 'area' not in kwargs.keys():
#         print(f"{kwargs.get('apt')},")
    
#     if 'state' in kwargs.keys() and  'country' in kwargs.keys():
#         print(f"{kwargs.get('country')} {kwargs.get('state')},")
#     elif 'state' not in kwargs.keys():
#         print(f"{kwargs.get('country')},")
#     elif 'country' not in kwargs.keys():
#         print(f"{kwargs.get('state')},")
    
#     if 'pincode' in kwargs.keys():
#         print(f"{kwargs.get('pincode')}.")



# shipping_label("raj","bhanderi",area ="park", apt ="xyz",state = "guj",
#                country ="india",pincode ="123456"
#                )


# fruits =["apple","pineapple","strawberry","grape"]

# fruit2 =[fruit[0] for fruit in fruits]

# print(fruit2)


# print(help(eg))

# print(eg.cube(10))
# print(__name__ )

