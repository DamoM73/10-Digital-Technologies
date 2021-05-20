# examples of working with text files

# write a string to a text file

with open("string.txt","w") as data_file:
    # "string.txt" is the file name
    # "w" means if the file exists it will overwrite the content with the new data
    # and if it doesn't exist, then a new file will be created.
    # data_file is the variable that the file is stored in, 
    # and how you reference it in your program

    data_file.write("This text will be written to the file\n") 

with open("string.txt","a") as data_file:
    # "string.txt" is the file name
    # "a" means if the file exists it will add new data to the end of the file
    # and if it doesn't exist, then a new file will be created.
    # data_file is the variable that the file is stored in, 
    # and how you reference it in your program

    data_file.write("This text should be added to the previous text")

with open("string.txt","r") as data_file:
    # "string.txt" is the file name
    # "r" means the file will be read

    all_the_data = data_file.read()
    # .read() reads and return all the data in file

    print(all_the_data)

with open("string.txt", "r") as data_file:
    # "string.txt" is the file name
    # "r" means the file will be read

    one_line_of_data = data_file.readline()
    # .readline() will read one line of the file
    print(one_line_of_data)

    the_next_line_of_data = data_file.readline()
    # using .readline() again will read the next line of the file
    print(the_next_line_of_data)

with open("string.txt", "r") as data_file:
    # "string.txt" is the file name
    # "r" means the file will be read

    data_in_list = data_file.readlines()
    # .readlines() will read all the data in the file
    # but each line will be stored as an element in a list
    print(data_in_list)
