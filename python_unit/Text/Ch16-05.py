# Ch16-05.py
phone_number = input("Please enter a phone number: ")

if len(phone_number) == 10 and phone_number.isdigit():
    print(phone_number[:4], phone_number[4:7], phone_number[7:])
else:
    print("This is not a phone number")
    
    
