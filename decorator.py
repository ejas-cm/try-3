# step 1: create a decorator:

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# step 2: Apply the decorator:

@my_decorator
def greet():
    print("Hello!")

greet()

# ----------------------------------------------

def decorator(func): 
    def wrapper(*args, **kwargs): 
        print("Starting...")
        result = func(*args, **kwargs) 
        print("Finished!")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(5, 3)) 


# ---------------------------------------------

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def message():
    return "hello"

print(message())
