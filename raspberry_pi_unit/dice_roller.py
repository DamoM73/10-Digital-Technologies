import random
import os
import time

def welcome():
    os.system('cls')
    print("Welcome to Dice Roller")
    print("=" * 22)

def collect_user_input(prompt, values):
    user_input = ""
    while user_input not in values:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
        except:
            user_input = ""
    return user_input

def num_dice():
    os.system('cls')
    return collect_user_input("How many dice are you rolling (max 100)? ", range(1,101))

def type_dice():
    os.system('cls')
    return collect_user_input("How many sides on the dice? (max 100)? ", range(1,101))


def roll(dice,dtype):
    total = 0
    os.system('cls')
    print("Rolling")
    for index in range(dice):
        roll = random.randint(1,dtype)
        print(f"Roll {index+1}: {roll}")
        total += roll
        time.sleep(.25)
    return total

def roll_total(dice,dtype,total):
    print(f"\n{dice} rolls of D{dtype} totalled {total}")
    input("\nPress <Enter> to continue")
    os.system('cls')

def men_help():
    os.system('cls')
    print("Select 1 to enter the number of dice you wish to roll (max 100)")
    print("Select 2 to enter the number of sides on your dice you wish to roll (max 100)")
    print("Select 3 to roll the dice")
    print("Select 4 to see this message")
    print("Select 5 to quit")
    input("\nPress <Enter> to continue")
    os.system('cls')


# ----- MAIN POROGRAM -----
welcome()

# --- main loop ---
running = True
dice = 1
dtype = 6
while running:
    print("Dice Roller Menu")
    print("-" * 16)
    print(f"Currently rolling {dice} D{dtype} dice.\n")
    print("1. Change number of dice")
    print("2. Change type of dice")
    print("3. Roll")
    print("4. Help")
    print("5. Quit\n")
    menu = collect_user_input("Please choose 1-5: ", range(1,6))
    
    if menu == 1:
        dice = num_dice()
    elif menu == 2:
        dtype = type_dice()
    elif menu == 3:
        total = roll(dice,dtype)
        roll_total(dice,dtype,total)
    elif menu == 4:
        men_help()
    elif menu == 5:
        running = False