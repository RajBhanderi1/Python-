#banking program

balance = 0.0


def show_balance():
    print(f"Your current Balance is : {balance:.2f}")
    
    

def deposit(x):
    global balance 
    balance += x  
    print(f"Your new current Balance is :{balance:.2f}")
    

def withdraw(y):
    global balance 
    balance -= y 
    print(f"Your new current Balance is :{balance:.2f}")
    

def exit_program():
    print("Thank you for using our Banking Service:")
       



while True :  
    print("=" * 35)
    print("         BANKING SERVICE")
    print("=" * 35)

    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("=" * 35)
    print()

    choice = input("Enter what you want to do : ")

    while choice not in ("1","2","3","4") :
        
        choice = input("Invalid input choose from 1,2,3,4 only :")
                         
    match choice:
            case "1" :
                show_balance()
                print()

            case "2":
                while True:
                    try:
                        x = float(input("Enter amount to deposit: "))

                        if x <= 0:
                            print("Enter a positive amount.")
                            continue

                        deposit(x)
                        break

                    except ValueError:
                        print("Numbers only!")    
                
            
            case "3":
                
              while True :
                try :
                    if balance == 0:
                        print("You dont have any money")
                        break

                    y = input(f"Enter amount to withdraw from {balance:.2f}: ")

                    y= float(y)
                    if y <=0 :
                        print("Enter positive numbers only.")
                        continue

                    elif y > balance:
                        print(f"Enter amount less than {balance:.2f} only.")
                        continue

                    withdraw(y)
                    break
                except ValueError:
                    print("Please enter digits only.")

            case "4":
                exit_program()
                break
            