# def my_function():
#     pass

def my_decorator(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise ValueError("First input position argument is not an integer")
        if not isinstance(args[1], int):
            raise ValueError("Second positional argument is not an integer")
        
        if len(kwargs) > 0:
            key_list = list(kwargs.keys())
            if not isinstance(kwargs[key_list[0]], int):
                raise ValueError("First optional argument is not an integer")
            if not isinstance(kwargs[key_list[1]], int):
                raise ValueError("Second optional argument is not an integer")
        else:
            kwargs.setdefault("c", 0)
            kwargs.setdefault("d", 0)
            

        return func(*args, **kwargs)
    return wrapper

@my_decorator
def addition(a, b, c, d):
    sum = a + b + c + d
    return sum 

print(addition(2, 3))
print(addition(2, 3, c=4, d=5))
# print(addition('a', 'b'))
# print(addition(2, 3, c='4', d=5))