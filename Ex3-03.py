# Ex3-03.py
import random

dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)

if dice_1 == dice_2:
    print("You rolled a double", dice_1)
    print("You scored", (dice_1 + dice_2) * 2)
else:
    print("You scored", dice_1 + dice_2)
    
