#DICT
# {}, keys, no duplicates allowed, ordered, mutable

my_dict = {
    "Name":"Rohan",
    "Age": 35,
    "Gender": "Male", 
    "Name": "Sohan"
}

# access 'Rohan'
print(my_dict['Name'])

# access 'Age'
print(my_dict["Age"])

# change value of Age to 25
my_dict["Age"] = 25
print(my_dict)

# access keys
print(my_dict.keys())

# access values
print(my_dict.values())

# access keys and value
print(my_dict.items())

############################################################
# ITEMS     SYMBOL      ORDERED     ACCESS      DUPLICATES      MUTABLE
# LIST        []           Y         Index         Y                Y
# DICT        {}           Y         Keys          N                Y
# TUPLE       ()           Y         Index         Y                N
# SETS        {}           N         -             N                N

