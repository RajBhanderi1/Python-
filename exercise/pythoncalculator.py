import math

operation = input("Enter Operation need to perform : +, -, *, /,%,sqrt, pow :")

if operation == "sqrt":

    try:
        num = float(input("Enter number : "))
        if num < 0:
            print("Invalid input. Please enter a positive number.")
        else:
            result = math.sqrt(num)
            print(f"Square root of {num} is : {result}")
    except ValueError :
        print("Invalid input enter numbers only")

elif operation == "pow":
    try:
        num1 = float(input("Enter base number : "))
        num2 = float(input("Enter power number : "))
        result = math.pow(num1,num2)
        print(f"{num1} to the power of {num2} is : {result}")
    except ValueError:
        print("Invalid input enter numbers only")
elif operation in ["+" ,"-",  "*" , "/", "%"]:

    try :
        num1= float(input("Enter first number : "))
        num2= float(input("Enter second number : "))


        add = num1 + num2
        sub = num1 - num2
        mul = num1*num2
        
        if operation == "+":
            print(f"Addition of {num1} and {num2} is : {add}")
        elif operation == "-" :
            print(f"Subtraction of {num1} and {num2} is : {sub}")
        elif operation == "*" :
            print(f"Multiplication of {num1} and {num2} is : {mul}")
        elif operation == "/" :
            try:
                div = num1/num2
                print(f"Division of {num1} and {num2} is : {div}")      
            except ZeroDivisionError:
                print("Cannot divide with zero")

        elif operation == "%" :
            try:
                remainder = num1%num2
                print(f"Remainder of {num1} and {num2} is : {remainder}")
            except ZeroDivisionError:
                print("Cannot divide with zero")

    except ValueError:
        print("Invalid input enter numbers only")
else:    
    print("Invalid operation")