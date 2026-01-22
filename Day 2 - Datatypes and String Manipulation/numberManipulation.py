x = round(3.738492) # Becomes 4
print(x)
y = round(3.14159) # Becomes 3
print(y)
z = round(3.14159, 2)
print(z)


# Assignment Operators
# Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
#
# +=
#
# -=
#
# *=
#
# /=

x = 5
x += 5
x -= 5
x *= 2
x /= 2

print(x)


# f-Strings
# In Python, we can use f-strings to insert a variable or an expression into a string.

age = 12

print(f"I am {age} years old")