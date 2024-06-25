# A lambda function to add two numbers
add = lambda x, y: x + y

# # Using the lambda function
# result = add(3, 5)
# print(result)  # Output: 8

# #Multiply argument a with argument b and return the result:
# mul = lambda a, b: a*b

# result = mul(4,5)
# print(result)

#Multiple Form with Pre Defined Value
# is_even_list = [lambda a=x*10: a for x in range(1,5)]
# for i in is_even_list:
#     print(i())

#Single Version with Argument Value
arg = 10
a = (lambda x: x)(1000)
print("Argument: ", a)


#Single Form with Predefined version
# riana = 100
# b = lambda a=riana: a
# print(b())
