def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mn(a, b):
    return a * b

def di(a, b):
    if b == 0:
        print("На нуль ділити не можна")
        return None
    return a / b

while True:
    num1 = input("Напишіть перше число (або 'q' для виходу): ")
    if num1.lower() == 'q':
        print("Програма завершена.")
        break

    dia = input("Виберіть дію (+, -, *, /) (або 'q' для виходу): ")
    if dia.lower() == 'q':
        print("Програма завершена.")
        break

    num2 = input("Напишіть друге число (або 'q' для виходу): ")
    if num2.lower() == 'q':
        print("Програма завершена.")
        break
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Будь ласка, введіть числа, а не текст.")
        continue

    if dia == "+":
        result = plus(num1, num2)
    elif dia == "-":
        result = minus(num1, num2)
    elif dia == "*":
        result = mn(num1, num2)
    elif dia == "/":
        result = di(num1, num2)
    else:
        print("Невідома дія. Спробуйте ще раз.")
        continue
    
    if result is not None:          
        print(f"Результат: {result}")
