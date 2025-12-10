import os
from unittest.mock import patch
from lab_02 import *

def test_insert_new_entry():
    student_directory = [
        {"name": "Alex", "phone": "0509876543", "email": "alex@gmail.com", "group": "CS-221"},
        {"name": "Sophia", "phone": "0981122334", "email": "sophia@gmail.com", "group": "CS-221"},
        {"name": "Liam", "phone": "0734455667", "email": "liam@gmail.com", "group": "AB-219"},
        {"name": "Noah", "phone": "0667788990", "email": "noah@gmail.com", "group": "CE-221"},
    ]
    with patch('builtins.input', side_effect=['Oliver', '0973344556', 'oliver@gmail.com', 'CS-221']):
        insert_new_entry(student_directory)
    assert student_directory[1]["name"] == "Oliver"
    assert student_directory[2]["name"] == "Sophia"

def test_modify_entry():
    student_directory = [
        {"name": "Alex", "phone": "0509876543", "email": "alex@gmail.com", "group": "CS-221"},
        {"name": "Sophia", "phone": "0981122334", "email": "sophia@gmail.com", "group": "CS-221"},
        {"name": "Liam", "phone": "0734455667", "email": "liam@gmail.com", "group": "AB-219"},
        {"name": "Noah", "phone": "0667788990", "email": "noah@gmail.com", "group": "CE-221"},
    ]
    with patch('builtins.input', side_effect=['Sophia', 'Ethan', '0956677889', 'ethan@gmail.com', 'CS-221']):
        modify_entry(student_directory)
    assert student_directory[1]["name"] == "Ethan"
    assert {"name": "Sophia", "phone": "0981122334", "email": "sophia@gmail.com", "group": "CS-221"} not in student_directory

def test_remove_entry():
    student_directory = [
        {"name": "Alex", "phone": "0509876543", "email": "alex@gmail.com", "group": "CS-221"},
        {"name": "Sophia", "phone": "0981122334", "email": "sophia@gmail.com", "group": "CS-221"},
        {"name": "Liam", "phone": "0734455667", "email": "liam@gmail.com", "group": "AB-219"},
        {"name": "Noah", "phone": "0667788990", "email": "noah@gmail.com", "group": "CE-221"},
    ]
    with patch('builtins.input', side_effect=['Liam']):
        remove_entry(student_directory)
    assert {"name": "Liam", "phone": "0734455667", "email": "liam@gmail.com", "group": "AB-219"} not in student_directory

def test_export_to_csv():
    student_directory = [
        {"name": "Alex", "phone": "0509876543", "email": "alex@gmail.com", "group": "CS-221"},
        {"name": "Sophia", "phone": "0981122334", "email": "sophia@gmail.com", "group": "CS-221"},
        {"name": "Liam", "phone": "0734455667", "email": "liam@gmail.com", "group": "AB-219"},
        {"name": "Noah", "phone": "0667788990", "email": "noah@gmail.com", "group": "CE-221"},
    ]
    test_filepath = 'test_lab2.csv'
    try:
        export_to_csv(test_filepath, student_directory)
        assert os.path.isfile(test_filepath)
        data = import_from_csv(test_filepath)
        assert data == student_directory
    finally:
        if os.path.exists(test_filepath):
            os.remove(test_filepath)