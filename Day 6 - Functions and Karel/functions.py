# A function in its simplest form is just a wrapper name for a block of code. You give it name and then when you call the function by that name, all the code within the function block will be executed. It can help us save time and reduce repeated code.
#
# Defining a new Function
# def <function name>():
#     print("Hello")
#     # Do something else
#     # Do something else ...
# Calling a Function
# Calling a function just means triggering the function. We can call a function at any point in our code in Python.

# <function name>()

# Types of functions :
# no returntype no args
# no returntype but args
# returntype but no args
# returntype and args

# indention in 4 spaces or a tab space python
def greet():
    print("Hello")

greet()


def say_my_name(name):
    print(f"you are {name}")

say_my_name("Heisenberg")

def sum(a,b):
    return a+b

print(sum(2,3))