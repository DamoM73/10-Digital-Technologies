# Ex5-03.py
name = input("Please enter student name: ")
marks = []
total = 0

for week in range(10):
    mark = int(input("Enter mark for week " + str(week + 1)+ ": "))
    total = total + mark
    marks.append(mark)
    
sorted_marks = sorted(marks, reverse = True)

print("\nStudent:", name)
print("Avg:", total / 10)
print("Max:", sorted_marks[-1])
print("Min:", sorted_marks[1])


    