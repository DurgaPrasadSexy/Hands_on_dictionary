from student_operations import add_student, display_students, search_student, remove_student, show_topper, display_sections

def menu():
    while True:
        print("\n--- School Data Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Roll Number")
        print("4. Remove Student by Roll Number")
        print("5. Show Class Topper")
        print("6. Display Unique Sections")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            show_topper()
        elif choice == "6":
            display_sections()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
