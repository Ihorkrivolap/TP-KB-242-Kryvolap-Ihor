def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "На нуль ділити не можна"
    return a / b

num1 = float(input("Напишіть перше число: "))
dia = input("Виберіть дію (+, -, *, /): ")
num2 = float(input("Напишіть друге число: "))

match dia:
    case '+':
        print(add(num1, num2))
    case '-':
        print(subtract(num1, num2))
    case '*':
        print(multiply(num1, num2))
    case '/':
        print(divide(num1, num2))
    case _:
        print("Невідома дія")