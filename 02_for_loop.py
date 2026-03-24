# normal for loop
for i in range(0, 3, 2):
    print(i)

# access list
my_list = [10, 20, 30, 40]
for i in my_list:
    print(i)

# access index of list
for i in range(len(my_list)):
    print(i)

# access list items and index
for i, val in enumerate(my_list):
    print(i, val)

my_dict = {
    "Name":"Rohan",
    "Age":35,
    "Gender":"Male"
}

# print keys and values
print(my_dict.keys())
print(my_dict.values())

# access keys and value seperately
for each_keys in my_dict.keys():
    print(each_keys)
for each_values in my_dict.values():
    print(each_values)

# access key value pair
for each_pair in my_dict.items():
    print(each_pair)

# access value with keys
for each_key in my_dict.keys():
    print(each_key, my_dict[each_key])