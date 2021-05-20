# Ex4-02.py
import random

for sets in range(1000):
    total = 0
    for index in range(10):
        num = random.randint(1,10)
        total = total + num
    average = total / 10
    print(average)
    

