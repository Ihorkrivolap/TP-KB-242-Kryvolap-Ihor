class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   
    
    def __str__(self):
        return f"Student: {self.name}, {self.age}"


group = [
    Student("John", 21),
    Student("Alice", 19),
    Student("Bob", 22),
    Student("Charlie", 20)
]

sorted_by_name = sorted(group, key=lambda s: s.name)

for s in sorted_by_name:
    print(s) 