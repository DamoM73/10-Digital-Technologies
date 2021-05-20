# Ex6-01.py
print("Please provide Dramamtic Socities' ticket sales")

total_tickets = 0

for index in range(4):
    tickets = -1
    while tickets < 0 or tickets > 120:
        tickets = input("Please enter tickets for show number", index+1)
        
        