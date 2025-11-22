def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Welcome to multi-step calculator")

# Step 1: First number
result = float(input("Enter first number: "))

while True:
    # Step 2: Ask for operator (including '=')
    operator = input("Select operator (+, -, *, /, =): ")

    # Step 3: If '=' → show answer and stop
    if operator == "=":
        final_answer = round(result, 2)
        print("Final result =", result)
        break

    # Step 4: Get next number
    next_num = float(input("Enter next number: "))

    # Step 5: Perform the operation
    if operator == "+":
        result = result + next_num
    elif operator == "-":
        result = result - next_num
    elif operator == "*":
        result = result * next_num
    elif operator == "/":
        if next_num == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = result / next_num
    else:
        print("Invalid operator!")


# Ask if the user wants to perform another calculation
next_calc = input(
    "Do you want to perform another calculation again? (yes/no): "
).lower()
if next_calc != "yes":
    print("Thank you for using the calculator. Goodbye!")
    exit()
