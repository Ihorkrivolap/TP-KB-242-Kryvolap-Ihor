import unittest
import os
from student import Student
from student_list import StudentList
from file_manager import FileManager

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.directory = StudentList()
        self.s1 = Student("Alex", "0509876543", "alex@gmail.com", "CS-221")
        self.s2 = Student("Sophia", "0981122334", "sophia@gmail.com", "CS-221")
        self.s3 = Student("Liam", "0734455667", "liam@gmail.com", "AB-219")
        
        self.directory.students.append(self.s1)
        self.directory.students.append(self.s2)
        self.directory.students.append(self.s3)
        self.directory.students.sort(key=lambda x: x.name)

    def test_add_student(self):
        new_student = Student("Oliver", "0973344556", "oliver@gmail.com", "CS-221")
        self.directory.add_student(new_student)
        
        all_students = self.directory.get_all()
        names = [s.name for s in all_students]
        
        self.assertIn("Oliver", names)
        self.assertEqual(names, ["Alex", "Liam", "Oliver", "Sophia"])

    def test_delete_student(self):
        result = self.directory.delete_student("Liam")
        self.assertTrue(result)
        
        all_students = self.directory.get_all()
        names = [s.name for s in all_students]
        self.assertNotIn("Liam", names)
        self.assertEqual(len(all_students), 2)

    def test_delete_non_existent_student(self):
        result = self.directory.delete_student("Zack")
        self.assertFalse(result)

    def test_update_student(self):
        new_version = Student("Ethan", "0956677889", "ethan@gmail.com", "CS-221")
        self.directory.update_student("Sophia", new_version)
        
        all_students = self.directory.get_all()
        names = [s.name for s in all_students]
        
        self.assertNotIn("Sophia", names)
        self.assertIn("Ethan", names)
        self.assertEqual(names, ["Alex", "Ethan", "Liam"])

class TestFileManager(unittest.TestCase):
    def test_save_and_load(self):
        filename = "test_lab3_data.csv"
        manager = FileManager(filename)
        students = [
            Student("Alex", "111", "a@a.com", "G1"),
            Student("Bob", "222", "b@b.com", "G2")
        ]
        
        manager.save_data(students)
        self.assertTrue(os.path.exists(filename))
        
        loaded_students = manager.load_data()
        self.assertEqual(len(loaded_students), 2)
        self.assertEqual(loaded_students[0].name, "Alex")
        self.assertEqual(loaded_students[1].email, "b@b.com")

        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    unittest.main()