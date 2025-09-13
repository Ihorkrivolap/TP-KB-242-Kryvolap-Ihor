import math
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Корінь 1: {x1}")
    print(f"Корінь 2: {x2}")
elif D == 0:
    x1 = -b / (2*a)
    print(f"Єдиний корінь: {x1}")
else:
    print("Немає дійсних коренів")