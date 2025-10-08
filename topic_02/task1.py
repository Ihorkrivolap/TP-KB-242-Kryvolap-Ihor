import math
def discriminant(a, b, c):
    return b**2 - 4 * a * c

def find_roots(a, b, c):
    D = discriminant(a, b, c)
    print(f"Дискримінант: {D}")
    
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Корені: x1 = {root1}, x2 = {root2}")
    elif D == 0:
        root = -b / (2 * a)
        print(f"Корінь: x = {root}")
    else:
        print("Немає дійсних коренів")
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))
find_roots(a, b, c)