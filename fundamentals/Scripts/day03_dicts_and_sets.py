"""
Part 1 — Dictionary
Create a dictionary called student with keys: name, age, grade, subjects (a list of 3 subjects)
Print each value using its key
Add a new key city and update the age by 1
Print all keys, all values, and all key-value pairs using loops

Part 2 — Set
Create two sets: classA and classB, each with 5 student names (2 names should overlap)
Print the union, intersection, and difference of the two sets
Check if a name is present in either set using the in keyword
Create a dictionary where each key is a subject name and each value is a set of student names enrolled in that subject
Print which students are in both the first and second subject
"""

#Task 1
student = {"name": "Arzaan", "age": 20, "grade" : "A" , "subjects": ["Maths" , "Physics" , "Computer_Science"]}
for key , value in student.items():
    print(f"{key.capitalize():<16} {str(value):<6}")

print(f"{'=' * 50}")
student.update({"age": 21, "city": "New_York"})
for key, value in student.items():
    print(f"{key.capitalize():<16} {str(value):<6}")
print(f"{'=' * 50}")

#Task 2
classA = {"Harry" , "James" , "Arzaan" , "Sakshi" , "Jane"}
classB = {"Arzaan" , "Sakshi" , "Meghan" , "Helena" , "Stewart"}

print(f"Union of the two classes is :{classA.union(classB)}")
print(f"Intersection of the two classes is :{classA.intersection(classB)}")
print(f"Difference of the two classes is :{classA.difference(classB)}")

x = "Henry"
if x in classA or x in classB:
    print(f"Yes, {x} was found!")
else:
    print(f"{x} was not found in either class.")

combined_dict = {
    "Maths" : {"Harry" , "James" , "Arzaan" , "Sakshi" , "Jane"},
    "Electronics":{"Arzaan" , "Sakshi" , "Meghan" , "Helena" , "Stewart"}
}

subject1_students = combined_dict.get("Maths")
subject2_students = combined_dict.get("Electronics")

intersection = subject1_students.intersection(subject2_students)
print(f"Students those who are enrolled in both the subjects is/are :{intersection}")

