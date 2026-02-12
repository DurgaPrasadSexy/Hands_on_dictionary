students = {}
def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        if roll in students:
            print("Roll Number already exists!")
            return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = tuple(map(int, input("Enter 3 subject marks separated by space: ").split()))
        if len(marks) != 3:
            print("Please enter exactly 3 marks.")
            return
        section = input("Enter Section: ")
        students[roll] = {"name": name, "age": age, "marks": marks, "section": section}
        print("Student added successfully!")
    except ValueError:
        print("Invalid input! Please enter numbers correctly.")

def display_students():
    if not students:
        print("No student records found.")
        return
    for roll, details in students.items():
        print(f"Roll: {roll}, Name: {details['name']}, Age: {details['age']}, Marks: {details['marks']}, Section: {details['section']}")

def search_student():
    try:
        roll = int(input("Enter Roll Number to search: "))
        if roll in students:
            details = students[roll]
            print(f"Found → Roll: {roll}, Name: {details['name']}, Age: {details['age']}, Marks: {details['marks']}, Section: {details['section']}")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input!")

def remove_student():
    try:
        roll = int(input("Enter Roll Number to remove: "))
        if roll in students:
            del students[roll]
            print("Student removed successfully!")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input!")

def show_topper():
    if not students:
        print("No student records found.")
        return
    topper = max(students.items(), key=lambda x: sum(x[1]["marks"]))
    roll, details = topper
    print(f"Topper → Roll: {roll}, Name: {details['name']}, Total Marks: {sum(details['marks'])}")

def display_sections():
    sections = {details["section"] for details in students.values()}
    print("Unique Sections:", sections)
