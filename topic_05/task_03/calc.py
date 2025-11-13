
from operations import get_numbers, perform_operation

def main():
    choice = input("Виберіть операцію (+, -, *, /): ")
    a, b = get_numbers()

    result = perform_operation(choice, a, b)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
