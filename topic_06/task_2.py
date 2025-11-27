import pprint
students = [
    {"ім'я": "John", "оцінка": 75},
    {"ім'я": "Alice", "оцінка": 95},
    {"ім'я": "Bob", "оцінка": 60},
    {"ім'я": "Eve", "оцінка": 95},
    {"ім'я": "Charlie", "оцінка": 88}
]

by_name = sorted(students, key=lambda s: s["ім'я"])
by_grade = sorted(students, key=lambda s: s["оцінка"])
print("За ім'ям:")
pprint.pprint(by_name)

print("\nЗа оцінкою:")
pprint.pprint(by_grade)