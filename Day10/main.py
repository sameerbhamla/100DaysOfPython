import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Whats the first number?: "))
    for symbol in operations:
        print(symbol)
    is_continuing = True

    while is_continuing:
        operation_symbol = input("pick an operation from the line above: ")
        num2 = float(input("Whats the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type n to exit.:  ").lower() == 'y':
            num1 = answer
        else:
            is_continuing = False
            calculator()


calculator()
