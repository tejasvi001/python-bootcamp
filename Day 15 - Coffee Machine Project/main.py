from data import items, ingredients_limit, ingredients_available, balance

# ---------------- MENU ----------------
def print_menu():
    """Prints available coffee menu"""
    print("\n☕ MENU ☕")
    for coffee, details in items.items():
        print(f"{coffee} for just ₹{details['cost']}")

# ---------------- ORDER COFFEE ----------------
def orderCoffee():
    try:
        print_menu()
        coffeeChoice = input("Enter an item to order: ").lower()

        if coffeeChoice not in items:
            print("❌ Item not found in menu")
            return

        if not check_ingredients_for_coffee(coffeeChoice):
            print(f"❌ Insufficient ingredients for {coffeeChoice}")
            return

        cost = items[coffeeChoice]["cost"]
        print(f"Please insert ₹{cost}")
        add_balance(cost)

        deduct_ingredients(coffeeChoice)
        print(f"✅ Here is your {coffeeChoice}. Enjoy!")

    except Exception as e:
        print("Unexpected error while ordering:", e)

# ---------------- INGREDIENT MANAGEMENT ----------------
def add_ingredients():
    try:
        while True:
            print_ingredients_add()
            item = input("Enter ingredient to add: ").lower()

            if item not in ingredients_limit:
                print("❌ Invalid ingredient")
                continue

            try:
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("❌ Quantity must be a number")
                continue

            limit = ingredients_limit[item] - ingredients_available[item]

            if qty > limit:
                print(f"❌ Limit exceeded. Max allowed: {limit}")
                continue

            ingredients_available[item] += qty
            print("✅ Ingredient added successfully")
            print_ingredients_available()

            if input("Add more? (yes/no): ").lower() == "no":
                break

    except Exception as e:
        print("Unexpected error in ingredient addition:", e)

# ---------------- BALANCE METHODS ----------------
def add_balance(amount):
    """Adds money to machine balance"""
    global balance
    balance += amount

def withdraw_balance():
    global balance
    try:
        check_balance()
        amount = int(input("Enter withdrawal amount: "))
        if amount > balance:
            print("❌ Insufficient balance")
        else:
            balance -= amount
            print("✅ Withdrawal successful")
    except ValueError:
        print("❌ Enter a valid number")

def check_balance():
    print(f"💰 Current balance: ₹{balance}")

# ---------------- INGREDIENT CHECKS ----------------
def check_ingredients_for_coffee(coffee):
    try:
        for ingredient, qty in items[coffee].items():
            if ingredient == "cost":
                continue
            if ingredients_available[ingredient] < qty:
                return False
        return True
    except KeyError:
        return False

def deduct_ingredients(coffee):
    for ingredient, qty in items[coffee].items():
        if ingredient != "cost":
            ingredients_available[ingredient] -= qty

# ---------------- DISPLAY METHODS ----------------
def print_ingredients_add():
    print("\nIngredients that can be added:")
    for i in ingredients_limit:
        print(f"{i}: {ingredients_limit[i] - ingredients_available[i]}")

def print_ingredients_limit():
    print("\nIngredient Limits:")
    for i in ingredients_limit:
        print(f"{i}: {ingredients_limit[i]}")

def print_ingredients_available():
    print("\nAvailable Ingredients:")
    for i in ingredients_available:
        print(f"{i}: {ingredients_available[i]}")

# ---------------- OPTIONS ----------------
def print_Options():
    print("""
1. Order Coffee
2. Check Balance
3. Check Available Ingredients
4. Check Ingredient Limits
5. Add Ingredients
6. Withdraw Balance
7. Exit
""")

# ---------------- MAIN LOOP ----------------
runMachine = True
while runMachine:
    print_Options()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Enter a number only")
        continue

    if choice == 1:
        orderCoffee()
    elif choice == 2:
        check_balance()
    elif choice == 3:
        print_ingredients_available()
    elif choice == 4:
        print_ingredients_limit()
    elif choice == 5:
        add_ingredients()
    elif choice == 6:
        withdraw_balance()
    elif choice == 7:
        runMachine = False
    else:
        print("❌ Invalid choice")
