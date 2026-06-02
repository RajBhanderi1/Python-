import random

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





