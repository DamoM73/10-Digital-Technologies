# number guessing game
import random

# print
print("Welcome to the number guessing game.")

# start main loop
while True:
    target = random.randint(1,100)
    guess = 0
    tries = 0
    print("Guess a number between 1 and 100\n")
    while guess != target:
        guess = input("Your guess: ")
        try:
            guess = int(guess)
        except:
            print("That is not a number\n")
        else:
            guess = int(guess)
            tries += 1
        
            if guess < target:
                print("Higher\n")
            elif guess > target:
                print("Lower\n")
    print(f"Correct, the number was {target}.\nIt took you {tries} guesses.\n")
    cont = ""
    while cont not in ["YES","NO"]:
        cont = input("Do you wish to continue? (Yes or No) ").upper()
    
    if cont == "NO":
        print("Goodbye")
        break
    
