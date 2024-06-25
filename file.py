# a file named "geek", will be opened with the reading mode.
file = open('test.txt', 'r')

# This will print every line one by one in the file
for each in file:
    print (each)

# Python code to illustrate read() mode character wise
file = open("test.txt", "r")
print (file.read(5))


with open('test.txt', 'r') as file:
    #data = file.readline()  # Only reads the first line of the file.
    data = file.readlines()    # Reads all lines one by one.
    for line in data:
        word = line.split()
        print (word)

# ************ File writing **************

file = open('test.txt', 'w')
file.write("This is a new line. ") #deleted earlier content and writes new line
print(file)
file.close()

# Appending to earlier content
file = open('test.txt', 'a') # a for appending
file.write("This is appended with the earlier content")
print(file)
file.close()

def create_file(file):
    try:
        with open(file, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + file + " created successfully.")
    except IOError:
        print("Error: could not create file " + file)


import os

def del_file(file):
    try:
        os.remove(file)
        print(file + " is deleted")
    except IOError:
        print("Could not delete: " + file)
create_file("test.txt")
del_file("test.txt")

create_file("test.txt")

with open("test.txt", 'r') as file2:
    print(file2)


