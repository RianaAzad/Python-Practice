#***************Creating string
# Using single quotes
single_quote_str = 'Hello, World!'

# Using double quotes
double_quote_str = "Hello, World!"

# Using triple single quotes
triple_single_quote_str = '''Hello,
World!'''

# Using triple double quotes
triple_double_quote_str = """Hello,
World!"""

#*********Accessing characters in string
my_string = "Hello, World!"
print(my_string[0])  # Output: H
print(my_string[7])  # Output: W

#********* Slicing string
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello
print(my_string[7:12]) # Output: World
print(my_string[:5])   # Output: Hello (same as my_string[0:5])
print(my_string[7:])   # Output: World! (same as my_string[7:len(my_string)])
print(my_string[:])    # Output: Hello, World! (same as the original string)


# *********** String methods ***********
my_string = "Hello, World!"

# Convert to uppercase
print(my_string.upper())  # Output: HELLO, WORLD!

# Convert to lowercase
print(my_string.lower())  # Output: hello, world!

# Check if the string starts with a substring
print(my_string.startswith("Hello"))  # Output: True

# Check if the string ends with a substring
print(my_string.endswith("World!"))  # Output: True

# Find the position of a substring
print(my_string.find("World"))  # Output: 7

# Replace a substring with another substring
print(my_string.replace("World", "Python"))  # Output: Hello, Python!

# Split the string into a list of substrings
print(my_string.split(", "))  # Output: ['Hello', 'World!']

# Join a list of strings into a single string
list_of_strings = ["Hello", "Python"]
print(", ".join(list_of_strings))  # Output: Hello, Python


# ********* Using f sting *********
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is John and I am 30 years old.


# ******* Immutable nature of string****
original_string = "Hello"
modified_string = original_string.replace("H", "J")

print(original_string)  # Output: Hello
print(modified_string)  # Output: Jello


# ******** Escape character *********
# Newline character
print("Hello\nWorld!")
# Output:
# Hello
# World!

# Tab character
print("Hello\tWorld!")
# Output: Hello   World!

# Including quotes
print("He said, \"Hello, World!\"")
# Output: He said, "Hello, World!"

print('It\'s a nice day!')
# Output: It's a nice day!
