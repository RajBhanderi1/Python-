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

# #Slot Machine

# def spin_row():
#     symbols =['😀','😁','🚀','💰']
#     result = []
#     # random.choice(symbols)
#     result =[random.choice(symbols) for x in range(3)]
#     print(" ".join(result))
#     # for x in result:
#     #     print(x)
#     if result == ['💰','💰','💰']:
#         print("You won")



# def main():
#     spin_row()

# if __name__ == '__main__':
#     main()

# from class_car import car

        
# car1 = car("toyota", "black",2,200000)

# car1.drive()
# car1.stop()

# class animals:
#     def __init__(self,name):
#         self.name= name
        
    
#     def eat(self):
#         print(f"{self.name} can eat")
#     def run(self):
#         print(f"{self.name} can run")
# class humans(animals):
#     def human(self):
#         print("I am human")


# class loyalty(humans):

#     def loyalty_level(self):
#         print(f"Level is 10")



# x = loyalty()

# x.loyalty_level()
# x.human()
# x.eat()
# x.run()

# class shape:
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled
          
# class circle(shape):
#     def __init__(self,color,is_filled,radius):
    
#         super().__init__(color,is_filled)
#         self.radius = radius
# class square(shape):
#         def __init__(self,color,is_filled,length):
#             super().__init__(color,is_filled)
#             self.length = length
            
# class triangle(shape):
#     def __init__(self,color,is_filled,width,height):

#             super().__init__(color,is_filled)
#             self.width = width
#             self.height = height


# s1 = circle("red",True,10)

# print(s1.color)
# print(s1.is_filled)
# print(s1.radius)

# class Animal:

#     def __init__(self, name):
#         self.name = name


# class Dog(Animal):

#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed


# dog1 =Dog("bull","german")


# print(dog1.name)
# print(dog1.breed)


# class books :
#     def __init__(self,name,author,pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
        
#     def __str__(self):
#         return f"{self.name} : {self.author}"
    
#     def __eq__(self,other):
#         return self.name == other.name and self.author == other.author
    
#     def __gt__(self, other):
#         return self.pages > other.pages
    
#     def __add__(self, other):
#         return self.pages + other.pages
    
#     def __sub__(self, other):
#         return self.pages - other.pages
    
#     def __contains__(self, keyword):
#         return keyword in self.name or keyword in self.author
#     def __getitem__(self, key):
       
#         if key == "name":
#             return self.name
       
#         elif key == "author" :
#             return self.author
#         elif key == "pages" :
#             return self.pages
#         else:
#             print("Invalid")
        
# book1 = books("The Hobbit","J.R.R. Tolkien",310)
# book2 = books("Harry Potter and the Philosopher's Stone","J.K. Rowling",252)


# print(book1['name'])

# class rectangle:
#     def __init__(self,width,height):
#         self._width = width
#         self._height =height

#     @property
#     def width(self):
#         return f"{self._width:.1f}"
#     @property
#     def height(self):
#         return f"{self._height:.1f}"
    
#     @width.setter
#     def width(self,new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("not a valid width")


#     @height.setter
#     def height(self,new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("not a valid height")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("height has been deleted")

# rec1 =rectangle(2,3)

# del rec1.width
# # print(rec1.width)
# print(rec1.height)


# def add_sprinkles(func):
#     def wrapper(*args,**kwargs):
#         print("you got sprinkles")
#         func(*args,**kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args,**kwargs):
#         print("you got fudge")
#         func(*args,**kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):

#     print(f"You got an {flavor} ice cream")

# get_ice_cream(flavor="vanilla")


#try except finally

# try:
#     num = int(input("Enter num to divide 1 by :"))
#     div =(1/num)
  
# except Exception:
#     print("enter number only")
# finally:
#       print("finnaly printed")
# # except ZeroDivisionError:
# #     print("dont enter 0")


#file handling
# import os
# file_path = "/home/arccus/Desktop/raj.txt"

# if os.path.exists(file_path):
#     print("File exists") 
#     if os.path.isfile(file_path):
#         print("Its a file")
#     elif os.path.isdir(file_path):
#         print("Its a folder")

# else :
#     print("Doesnt exists")

# import csv
# import os
# import json

# employees = [
#                 ["Name","age","Height"],
#                 ["hi","hello","bye"],
#                 ["a","b","c"]
#             ]
# # # file_data = "Hello this is the file's first line"
# # file_data = {"name": "Spongebob", "job": "Fry Cook",
# #                 "age": "Patrick", "jonb": "None"}
            

# file_path ="/home/arccus/Desktop/rajfolder/output.json"
# try :

#     with  open(file_path,"w") as file :
   
#     #     # this for plain files::

#     #     # file.write(file_data)
#     #     # print("data written")  

#     #     # this for json files::
   
#             # json.dump(file_data,file,indent= 4)  

#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
    
#     if os.path.exists(file_path):
#         with open(file_path,"r") as file:
#             content = csv.reader(file)
#             for line in content:
#                 print(line[0],line[1])
        
#     else :
#        print("Create file first")
        
# except FileExistsError:
#     print("files exists change the name of file ")
# except FileNotFoundError:
#    print("File not found")

# except PermissionError:
#    print("You dont have permission")



# import datetime

# today = datetime.date.today()
# now = datetime.datetime.now()

# date = datetime.datetime(2025,12,10)
# # print(date)
# time = datetime.time(12,20,10)
# # print(time)

# # now = now.strftime("%H:%M:%S ; %d:%m:%Y")

# # target_date = datetime.datetime.

# #   print(now)
# if now < date:
#     print("you have time")
# elif now> date:
#     print("Your time is over")

# else:
#     print("Right on time") 

# import pygame
# import time 
# import datetime

# def alarm_time_f(alarm_time):
#     print(f"Alarm set for {alarm_time}.")
    

#     running = True
#     while running :
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)
#         time.sleep(1)

#         if current_time == alarm_time:
#             print("Wake up")
#             running =False





# def main():
#     alarm_time = input("Enter time:")
#     alarm_time_f(alarm_time)

# if __name__ == "__main__":
#     main()
# import threading

# def walk_dog(x,y,z):
#     time.sleep(10)
#     print(f"walking {x} {y} {z} completed")

# def get_mail():
#     time.sleep(3)
#     print("got mail")

# def throw_trash():
#     time.sleep(6)
#     print("Throwed trash")

# chore1 = threading.Thread(target=walk_dog,args =(target = "doo","doo","doo"))
# chore1.start()

# chore2 = threading.Thread(target=get_mail)
# chore2.start()

# chore3 = threading.Thread(target=throw_trash)
# chore3.start()

# chore1.join()
# chore2.join()
# chore3.join()

# print("done")

# import requests

# def get_pokemon_info(name):
#     base_url = "https://pokeapi.co/api/v2/"
#     url = f"{base_url}pokemon/{name}"
#     response = requests.get(url)

#     if response.status_code  == 200:
#         pokemon_data = response.json()

#         return pokemon_data
    
#     else:
#          print(f"Data not retrieved\nError : {response.status_code}")   
# def main():
#         pokemon_name = "typhlosion"
#         pokemon_info = get_pokemon_info(pokemon_name)
#         if pokemon_info:
#             print(f"Name: {pokemon_info["name"].capitalize()}")
#             print(f"Height: {pokemon_info["height"]}")
#             print(f"Weight: {pokemon_info["weight"]}")

# if __name__ == "__main__":
#     main()


# import os
# os.environ["QT_QPA_PLATFORM"] = "wayland"

# import sys
# from PyQt5.QtWidgets import QApplication,QMainWindow


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
    
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show() 
#     print("opened screen")
    
#     print(app.exec_())
#     # print("opened screen")
#     # sys.exit()
# if __name__ == "__main__":
#     main()
import os
os.environ["QT_QPA_PLATFORM"] = "wayland"

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hey")
        self.resize(400,400)
        self.setWindowIcon(QIcon("/home/arccus/Python/Python-/Screenshot From 2026-06-10 10-32-06.png"))
        label = QLabel("Hello",self)
        # label2 =QLabel("Bye",self)
        label.setFont(QFont("Times New Roman",25))
        label.setGeometry(0,0,400,400)
        label.setStyleSheet("color : #fccf03;"
                            "background-color : blue;"
                            "font-style : italic;"
                            "font-weight : Bold;"
                            "text-decoration : underline;")
        
        label.setAlignment(Qt.AlignCenter)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
