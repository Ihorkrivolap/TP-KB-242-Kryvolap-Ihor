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
        a_str = input("Введіть перше число: ")
        try:
            a = float(a_str)
        except ValueError:
            print("Будь ласка, введіть числа, а не текст.")
            continue
        
        operation = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ")
        if operation.lower() == 'q':
            return None, None, None 
        if operation not in ['+', '-', '*', '/']:
            print("Невідома операція!")
            continue
        
        b_str = input("Введіть друге число: ")
        try:
            b = float(b_str)
        except ValueError:
            print("Будь ласка, введіть числа, а не текст.")
            continue
        
        return operation, a, b

def main():
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
    