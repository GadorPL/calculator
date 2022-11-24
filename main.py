from art import logo

# Calculator
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    calculating = True
    while calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again.: ")
        if choice.lower() == 'y':
            num1 = answer
        else:
            calculating = False
            calculator()


calculator()
