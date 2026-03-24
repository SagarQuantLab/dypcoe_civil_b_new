# string slicing

my_string = "This is Civil students"
# ['T', 'h', 'i'......]
#   0    1    2
# first letter access
print(my_string[0])

# access word 'This'
print(my_string[0:4])

# access only 'T and i'
print(my_string[0:4:2])

# access 'C'
print(my_string[8])

# access last 's'
print(my_string[-1])

# reverse string
print(my_string[::-1])

# reverse only 'students'
print(my_string[:-9:-1])

# capital letters/Upper case
print(my_string.upper())

# lower case
print(my_string.lower())

# replace 's' with 'X'
print(my_string.replace('s', 'X'))
