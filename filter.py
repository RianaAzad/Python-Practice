'''
Syntax: filter(func, iterable)

The following points are to be noted regarding filter():

Unlike map(), only one iterable is required.
The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it. Also, as only one iterable is required, it's implicit that func must only take one argument.
filter passes each element in the iterable through func and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".
'''

#---Finding Palindrome----
elements = ["12321", 'Riana', 'abba', 'Abba', 'sdfgfds']
palindrome = list(filter(lambda word: word.lower() == word[::-1].lower(), elements))
print(palindrome)


