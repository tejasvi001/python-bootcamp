# scope is just area of usage of a variable
# Local Scope: Inside the function,
# Global Scope : accessible throughout the code/file
# Python does not have the concept of block scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


#Modify Variables with global scope
def increase_enemies2():
    global enemies
    enemies = 4
    print(f"enemies inside function 2: {enemies}")

increase_enemies2()
print(f"enemies outside function: {enemies}")

