# while loop example
test_result = int(input("Please enter test result: "))

# Set maximum and minimum to first test result
max_result = test_result
min_result = test_result

while test_result != -1:
    # check for new maxand min
    if test_result > max_result:
        max_reult = test_result
    elif test_result < min_result:
        min_result = test_result
        
    # get next result value
    test_result = int(input("Please enter test result (-1 to finish): "))
    
# print results
print("\nMaximum test result =", max_result)
print("Minimum test result =", min_result)