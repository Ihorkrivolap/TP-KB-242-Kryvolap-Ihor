def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе!")
        return None 

def get_user_input():
    while True:
        try:
            a = float(input("Введіть перше число: "))
            operation = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")
            if operation.lower() == 'q':
                return None, None, None 
            if operation not in ['+', '-', '*', '/']:
                raise ValueError("Невідома операція!")
            b = float(input("Введіть друге число: "))
            return operation, a, b
        except ValueError:
            print("Будь ласка, введіть числа, а не текст.")

while True:
    operation, a, b = get_user_input()
    if operation is None:
        print("Вихід з програми.")
        break
    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '/':
        result = divide(a, b)
        if result is None:
            continue 
    elif operation == '*':
        result = multiply(a, b)
    print(f"Результат: {result}")