'''
Class is a blueprint - it defines the structure(methods and attributes) for an object.
Syntax: class Car:
Class - PascalCase
functions - camelCase
everything else - snake_case
Object creation - Needs a () - to call a constructor.

Method is just a function associated with a class


Constructor -
def __init__(self):
# initialize attributes



self in python is same as this in java
'''

class User:
    username=""

    def __init__(self,username):
        self.username=username
        
    def greet(self_):
        print(f"Hello {self_.username}")

user1= User("Tejasvi")
user1.greet()