import json
import re
from abc import ABC,abstractmethod
from pathlib import Path

database = "school_data.json" # This is our main original database where existing and updated data is stored.
data = {"students" : [] , "teachers" : [] } # This is the dummy data

if Path(database).exists():
    with open(database , 'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(database , 'w') as file:
        json.dump(data, file , indent=4)

class Persons(ABC):
    @abstractmethod
    def get_roles(self):
        pass
    @abstractmethod
    def register(self):
        pass
    @abstractmethod
    def show_details(self):
        pass
    @staticmethod
    def validate_email(email):
        if re.match(r"[a-zA-Z0-9]+@[a-zA-Z]+\.com", email):
            return True
        else:
            return False


class Student(Persons):
    def get_roles(self):
        return "Student"
    def register(self):
        name = input("Please enter your name:- ")
        age = input("Please enter your age:- ")
        email = input("Please enter your email:- ")
        roll_no = input("Please enter your roll no:- ")
        if not Persons.validate_email(email):
            print("Invalid email")
            return
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                print("Student already registered")
                return

        data['students'].append({
            "roll_no" : roll_no,
            "name" : name,
            "age" : age,
            "email" : email,
            "grades" : {}
        })
        save()
        print(f"Student {name} has been registered successfully!")

    def add_grades(self):
        roll_no = input("Please enter your roll no:- ")
        subject = input("Please enter your subject:- ")
        marks = input("Please enter your marks:- ")
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                i["grades"][subject] = marks
                save()
                print(f"Student {i['roll_no']} has been graded successfully!")
                return
            else:
                print("Invalid roll no or Student does not exist!")

    def show_details(self):
        roll_no = input("Please enter your roll no:- ")
        for s in data["students"]:
            if s["roll_no"] == roll_no:
                grades = s['grades']
                avg = sum(grades.values()) / len(grades) if grades else 0

                print(f"\n  Name    : {s['name']}")
                print(f"  Roll no : {s['roll_no']}")
                print(f"  Grades  : {grades}")
                print(f"  Average : {avg:.1f}")
                return


class Teacher(Persons):
    def get_roles(self):
        return "Teacher"
    def register(self):
        name = input("Please enter your name:- ")
        age = input("Please enter your age:- ")
        email = input("Please enter your email:- ")
        subject = input("Please enter your subject:- ")
        emp_id = input("Please enter your employee id:- ")
        if not Persons.validate_email(email):
            print("Invalid email")
            return
        for i in data["teachers"]:
            if i["emp_id"] == emp_id:
                print("Teacher already registered")
                return

        data["teachers"].append({
            "name": name,
            "age": age,
            "email": email,
            "subject": subject,
            "emp_id" : emp_id
        })
        save()
        print(f"Teacher {name} has been registered successfully!")

    def show_details(self):
        emp_id = input("Employee ID: ")

        for t in data["teachers"]:
            if t["emp_id"] == emp_id:
                print(f"\n  Name  : {t['name']}")
                print(f"  Subject : {t['subject']}")
                print(f"  Emp ID  : {t['emp_id']}")
                return
        print("Teacher not found.")


teacher= Teacher()
student = Student()

print("press 1  to register a student")
print("press 2  to register a teacher")
print("press 3  to add grades")
print("press 4  to show a student detail")
print("press 5  to show a teacher detail")


choice = int(input("please tell your choice :- "))
if choice == 1:
    student.register()
elif choice == 2:
    teacher.register()
elif choice == 3:
    student.add_grades()
elif choice == 4:
    student.show_details()
elif choice == 5:
    teacher.show_details()