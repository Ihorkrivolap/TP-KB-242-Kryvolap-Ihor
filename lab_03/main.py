import sys
from student import Student
from student_list import StudentList
from file_manager import FileManager

def print_directory(student_list):
    for student in student_list.get_all():
        print(student)

def get_student_input(prompt_name=None):
    if prompt_name:
        name = prompt_name
    else:
        name = input("Please enter student name: ")
    
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    return Student(name, phone, email, group)

def run_program():
    filepath = sys.argv[1]
    
    file_manager = FileManager(filepath)
    directory = StudentList()
    
    loaded_data = file_manager.load_data()
    for s in loaded_data:
        directory.students.append(s)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ").lower()

        if choice == "c":
            print("New element will be created:")
            new_student = get_student_input()
            directory.add_student(new_student)
            print("New element has been added")
            print_directory(directory)

        elif choice == "u":
            print("Existing element will be updated")
            name_to_update = input("Please enter name to be updated: ")
            
            if directory.find_student_index(name_to_update) == -1:
                print("Element was not found")
            else:
                new_name = input("Please enter new student name: ")
                updated_student = get_student_input(new_name)
                directory.update_student(name_to_update, updated_student)
                print("Element has been updated")
                print_directory(directory)

        elif choice == "d":
            print("Element will be deleted")
            name_to_delete = input("Please enter name to be deleted: ")
            if directory.delete_student(name_to_delete):
                print(f"Student {name_to_delete} deleted.")
            else:
                print("Element was not found")
            print_directory(directory)

        elif choice == "p":
            print("List will be printed")
            print_directory(directory)

        elif choice == "x":
            print("Exit()")
            file_manager.save_data(directory.get_all())
            break

        else:
            print("Wrong choice")

if __name__ == "__main__":
    run_program()