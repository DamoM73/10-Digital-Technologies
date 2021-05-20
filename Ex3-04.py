# Ex3-04.py
amount = float(input("Please enter purchase amount: "))

if amount >= 200.0:
    discount = amount * .1
elif amount >= 100.0:
    discount = amount * .05
else:
    discount = 0
    
print("\nPurchase amount:", amount)
print("Discount:", discount)
print("Amount owed:", amount - discount)

