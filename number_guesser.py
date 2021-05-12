import random

print("Welcome to the number guessing game.")
running = True
while running:
    rand_num = random.randint(1,100)
    guess = 0
    tries = 0
    while guess != rand_num:
        guess = input("Enter guess: ")
        try:
            int(guess)
        except:
            print("This is not a number")
        else:
            guess = int(guess)
            tries += 1
            if guess < rand_num:
                print("Higher")
            elif guess > rand_num:
                print("Lower")
            else:
                print(f"Correct, the number was {rand_num}. You had {tries} guesses.\n")
                cont = input("Do you wish to continue> (Yes or No) ")
                if cont == "No":
                    print("Thank you for playing")
                    running = False
                    
            