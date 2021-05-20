# Ex3-01.py
length = float(input("Please enter length: "))
width = float(input("Please enter width: "))

area = length * width

if length == width:
    print("This is a square of area", area)
else:
    print("This is a rectangle of area", area)
    
    