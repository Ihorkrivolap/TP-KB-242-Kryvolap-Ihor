
from functions import add, subtract, multiply, divide

def get_numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    return a, b

def perform_operation(choice, a, b):
    if choice == '+':
        return add(a, b)
    elif choice == '-':
        return subtract(a, b)
    elif choice == '*':
        return multiply(a, b)
    elif choice == '/':
        return divide(a, b)
    else:
        return "Невірний вибір операції!"
