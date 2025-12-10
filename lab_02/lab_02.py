import sys
import csv

def import_from_csv(filepath):
    directory = []  
    with open(filepath) as file:
        reader = csv.DictReader(file)
        for row in reader:
            directory.append({
                "name": row["Name"],
                "phone": row["Phone"],
                "email": row["Email"],
                "group": row["Group"]
            })
    return directory

def export_to_csv(filepath, directory):
     with open(filepath, "w", newline='') as csvfile:
        fieldnames = ["Name", "Phone", "Email","Group"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in directory:
            writer.writerow({
                "Name": entry["name"],
                "Phone": entry["phone"],
                "Email": entry["email"],
                "Group": entry["group"]
            })

def display_all_directory(directory):
    for elem in directory:
        strForPrint = "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + ", Email is " + elem["email"] + ", Group is " + elem["group"]
        print(strForPrint)
    return

def insert_new_entry(directory):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newEntry = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = 0
    for item in directory:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    directory.insert(insertPosition, newEntry)
    print("New element has been added")
    return

def remove_entry(directory):
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for i, item in enumerate(directory):
        if name == item["name"]:
            deletePosition = i
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del directory[deletePosition]
    return

def modify_entry(directory):
    name = input("Please enter name to be updated: ")
    deletePosition = -1
    for i, item in enumerate(directory):
        if name == item["name"]:
            deletePosition = i
            break
    if deletePosition == -1:
        print("Element was not found")
        return
   
    del directory[deletePosition]
    new_name = input("Please enter new student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newEntry = {"name": new_name, "phone": phone, "email": email, "group": group}
   
    insertPosition = 0
    for item in directory:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    directory.insert(insertPosition, newEntry)
    print("Element has been updated")
    return

def run_program():
    if len(sys.argv) < 2:
        print("Usage: python lab_02.py <csv_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    directory = import_from_csv(filepath)
    
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        chouse = chouse.lower()
        if chouse == "c":
            print("New element will be created:")
            insert_new_entry(directory)
            display_all_directory(directory)
        elif chouse == "u":
            print("Existing element will be updated")
            modify_entry(directory)
            display_all_directory(directory)
        elif chouse == "d":
            print("Element will be deleted")
            remove_entry(directory)
            display_all_directory(directory)
        elif chouse == "p":
            print("List will be printed")
            display_all_directory(directory)
        elif chouse == "x":
            print("Exit()")
            export_to_csv(filepath, directory)
            break
        else:
            print("Wrong choice")
            
if __name__ == "__main__":
    run_program()