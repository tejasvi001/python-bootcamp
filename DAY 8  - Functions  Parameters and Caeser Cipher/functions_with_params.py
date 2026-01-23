# name is the parameter(place holder)
# while Tejas is argument (actual data passed)
def greet(name):
    print(f"Hello {name}")

greet("Tejas")

#functions with more than one params
def greet(name,location):
    print(f"Hello {name}")
    print(f"How it is to be in {location}")

#positional arguments
# means first arg to first param, second to second and nth to nth
greet("Tejas","Rajgarh")

#Keyword Arguments
#passing the value to a parameter explicitly with its name order doesnt matter
greet(location="Rajgarh", name="Tejas")