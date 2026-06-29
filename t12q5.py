def student_database():
    students = {}  # dictionary with roll_no as key
    
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add student")
        print("2. Search student by roll number")
        print("3. Display all students")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                # Add student
                try:
                    roll_no = int(input("Enter roll number: "))
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    city = input("Enter city: ")
                    
                    # Use update() to add student record
                    students.update({roll_no: {"name": name, "age": age, "city": city}})
                    print("Student added successfully!")
                except ValueError:
                    print("Invalid input! Roll number and age must be numeric.")
            
            elif choice == 2:
                # Search student
                try:
                    roll_no = int(input("Enter roll number to search: "))
                    student = students.get(roll_no)
                    if student:
                        print("Student found:", student)
                    else:
                        print("No student found with this roll number.")
                except ValueError:
                    print("Invalid input! Roll number must be numeric.")
            
            elif choice == 3:
                # Display all students
                if students:
                    print("\n--- All Students ---")
                    for roll, info in students.items():
                        print(f"Roll No: {roll}, Name: {info['name']}, Age: {info['age']}, City: {info['city']}")
                else:
                    print("No student records available.")
            
            elif choice == 4:
                # Exit
                print("Exiting Student Database. Goodbye!")
                break
            
            else:
                print("Invalid choice! Please enter between 1 and 4.")
        
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")


# Run the function
student_database()
