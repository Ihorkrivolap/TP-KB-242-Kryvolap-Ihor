import functions  

class Calculator:
    def __init__(self):
        self.log_file = "log.txt" 
    
    def get_numbers(self):
        try:
            n1 = float(input("Введіть перше число: "))
            n2 = float(input("Введіть друге число: "))
            return n1, n2
        except ValueError:
            print("Помилка: введіть дійсні числа.")
            return None, None
    
    def select_operation(self, operator, x, y):
        if operator == '+':
            return functions.add(x, y)
        elif operator == '-':
            return functions.subtract(x, y)
        elif operator == '*':
            return functions.multiply(x, y)
        elif operator == '/':
            return functions.divide(x, y)
        else:
            return "Невідома операція"
    
    def save_log(self, x, y, op, res):
        with open(self.log_file, "a") as file:
            file.write(f"{x} {op} {y} = {res}\n")
    
    def run(self):
        while True:
            op = input("Введіть знак (+, -, *, /) або 'q': ").strip()
            
            if op == 'q':
                print("Роботу завершено.")
                break
            
            if op not in ('+', '-', '*', '/'):
                print("Невірна дія.")
                continue
            
            x, y = self.get_numbers()
            if x is None or y is None:
                continue
            
            result = self.select_operation(op, x, y)
            print(f"Результат: {result}")
            
            self.save_log(x, y, op, result)