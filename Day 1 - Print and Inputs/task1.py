#use of print statement
print("Hello World")


#use of \n character for a new line
print("Hello World \nthis is a new line")

#use of input method to take input

print("Hello"+input("What is your name"))


#take input store it in a variable and display its length

# Rules of variable naming in Python.

# Make sure your variable names are descriptive
# Don't have spaces between words
# Don't start with numbers
# Don't use special words like print or input
# Choose simple words that are less likely to become typos
# Check the company style guidelines if you start work at a company

name=input("What is your good name")
length=len(name)
print("Your name is "+str(length)+" characters long")

# Create a greeting for your program.
# Ask the user for the city that they grew up in and store it in a variable.
# Ask the user for the name of a pet and store it in a variable.
# Combine the name of their city and pet and show them their band name.

city=input("What city did you grew up in")
pet=input("What do you call your pet")
print("Your Band name could be " + city +" "+ pet)