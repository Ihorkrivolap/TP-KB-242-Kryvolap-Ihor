import functions

def select_operation(operator, x, y):
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
    