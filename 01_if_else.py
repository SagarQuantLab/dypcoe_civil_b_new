# IF ELSE

my_age = 18
if my_age > 18:
    print("Adult")

# If else
if my_age> 18:
    print("Adult")
else:
    print("Minor")

if my_age> 18:
    print("Adult")
elif my_age == 18:
    print("Turning Adult")
else:
    print("Minor")

# reducing/removing else
my_age = 18
msg = "Bye"
if isinstance(my_age, int):
    msg = "Hello"

print(msg)