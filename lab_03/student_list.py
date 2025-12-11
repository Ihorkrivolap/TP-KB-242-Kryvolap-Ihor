from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def get_all(self):
        return self.students

    def add_student(self, student: Student):
        insert_position = 0
        for item in self.students:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)

    def find_student_index(self, name):
        for i, student in enumerate(self.students):
            if student.name == name:
                return i
        return -1

    def delete_student(self, name):
        index = self.find_student_index(name)
        if index != -1:
            del self.students[index]
            return True
        return False

    def update_student(self, old_name, new_student: Student):
        delete_result = self.delete_student(old_name)
        if delete_result:
            self.add_student(new_student)
            return True
        return False