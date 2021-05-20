# Ch15-02.py

# Set maximum and minimum to first test result
test_result = 0
max_result = 0
min_result = 100

while test_result != -1:           # loop will continue until user enters -1
    # get result value
    test_result = int(input("Please enter test result (-1 to finish): "))
        
    # check for new max and min 
    if test_result > max_result:
        max_result = test_result
    if test_result < min_result and test_result != -1:
        min_result = test_result
    
# print results
print("\nMaximum test result =", max_result)
print("Minimum test result =", min_result)


