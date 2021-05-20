# Ex4-03.py
total_ab = 0
total_00 = 0

while True:
    code = input("Please enter product code (q to exit): ").upper()
    
    if code == "Q":
        break
    
    if len(code) != 5 or not (code[:2] == "AB" or code[:2] == "AS") or not code[2:].isdigit():
        print("\nInvalid code. Code must start with AB or AS and finish with 3 digits\n")
    else:
        if code[:2] == "AB":
            total_ab = total_ab + 1
        if code[3:] == "00":
            total_00 = total_00 + 1
    
print("Total AB code", total_ab)
print("Total codes ending in 00", total_00)

