import math

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

age = int(input("Enter your age : "))

if age>18 :
    print("An adult")
elif age>20 and age<30 :
    print("You are in your twenties")
else:
    print(" not an adult")

