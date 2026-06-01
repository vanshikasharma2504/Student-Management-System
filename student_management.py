students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    print("5. Delete Student")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll] = name
        print("Student Added Successfully")

    elif choice == "2":
        print("\nStudent Records:")
        for roll, name in students.items():
            print(roll, "-", name)

    elif choice == "3":
        roll = input("Enter Roll Number: ")
        if roll in students:
            print("Student Name:", students[roll])
        else:
            print("Student Not Found")

    elif choice == "4":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")
