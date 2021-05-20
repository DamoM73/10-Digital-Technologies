# Ex4-01.py
import random

total = 0

for index in range(10):
    num = random.randint(1,10)
    print(num)
    total = total + num
    
print("\nTotal:", total)

