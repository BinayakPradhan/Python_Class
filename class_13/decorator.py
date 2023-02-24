def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("John")
In this example, my_decorator is a decorator function that takes a function as an argument and returns a wrapper function that adds some behavior before and after calling the original function. The @my_decorator syntax above the say_hello function is called a "decorator"
