# Ex5-02.py
names = []
name = ""
while name.lower() != "end":
    name = input("Please enter a name (End to finish): ")
    names.append(name)
    
first_half = names[:len(names)//2]

if len(first_half) % 2 != 0:
    print(first_half[0])
else:
    print(first_half)
    
