import csv
from student import Student

class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        students = []
        
        with open(self.filepath, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name=row["Name"],
                        phone=row["Phone"],
                        email=row["Email"],
                        group=row["Group"]
                    )
                    students.append(student)

        return students

    def save_data(self, students):
        with open(self.filepath, 'w', newline='',) as csvfile:
            fieldnames = ["Name", "Phone", "Email", "Group"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    "Name": student.name,
                    "Phone": student.phone,
                    "Email": student.email,
                    "Group": student.group
                })