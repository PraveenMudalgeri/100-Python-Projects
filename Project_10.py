from art import logo10

def calculation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return 'Invalid operator'


def calculator():
    print(logo10)
    num1 = float(input('Enter the first number: '))
    continue_calculation = True
    while continue_calculation:
        num2 = float(input('Enter the second number: '))
        operator = input("Enter a operator ('+','-','*','/'): ")
        if num2 == 0 and operator == '/':
            print('Cannot divide by zero')
            continue_calculation = False
        result = calculation(float(num1), float(num2), operator)
        if result == 'Invalid operator':
            print('Invalid operator')
            continue_calculation = False
        print(f'{num1} {operator} {num2} = {result}')
        user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if user_choice == 'y':
            num1 = result
        else:
            continue_calculation = False
    calculator()

calculator()
