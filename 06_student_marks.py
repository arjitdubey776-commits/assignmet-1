students = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 78
}

name = input("Enter student name: ")

if name in students:
    print(name, "scored", students[name])
else:
    print("Student not found")
