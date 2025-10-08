

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mn(a, b):
    return a * b

def di(a, b):
    if b == 0:
        print("На нуль ділити не можна")
    return a / b

num1 = float(input("Напишіть перше число: "))
dia = input("Виберіть дію (+, -, *, /): ")
num2 = float(input("Напишіть друге число: "))

if dia == "+":
    result = plus(num1, num2)
elif dia == "-":
    result = minus(num1, num2)
elif dia == "*":
    result = mn(num1, num2)   
elif dia == "/":
    result = di(num1, num2)
else:
    print("невідома дія")

print(result)