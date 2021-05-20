# Ex5-04.py
monthly_avg= [["January",6,3],
              ["Febuary", 7,3],
              ["March",10,4],
              ["April",13,6],
              ["May",17,9],
              ["June",20,12],
              ["July",22,14],
              ["August",21,14],
              ["September",19,12],
              ["October",14,9],
              ["November",10,6],
              ["December",7,3]]

lowest = monthly_avg[0]
highest = monthly_avg[0]

for month in monthly_avg:
    if month[2] < lowest[2]:
        lowest = month
    if month[1] > highest[1]:
        highest = month
        
print("The hotest average temp was", highest[1], "in", highest[0])
print("The lowest average temp was", lowest[1], "in", lowest[0])

