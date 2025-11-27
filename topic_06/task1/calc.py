from operations import select_operation

def save_log(x, y, op, res):
    with open("log.txt", "a") as file:
        file.write(f"{x} {op} {y} = {res}\n")

def get_numbers():
    n1 = float(input("Введіть перше число: "))
    n2 = float(input("Введіть друге число: "))
    return n1, n2

def main():
    while True:
        op = input("Введіть знак (+, -, *, /) або 'q': ").strip()
        
        if op == 'q':
            print("Роботу завершено.")
            break
            
        if op not in ('+', '-', '*', '/'):
            print("Невірна дія.")
            continue
            
        x, y = get_numbers()
        
        result = select_operation(op, x, y)
        print(f"Результат: {result}")
        
        save_log(x, y, op, result)

main()