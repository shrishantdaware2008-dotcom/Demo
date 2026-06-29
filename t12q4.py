class Student:
    def __init__(self, name, roll_no):
        # Initialize student attributes
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []  # empty list to store marks

    def add_mark(self, mark):
        try:
            # Convert input to float to handle numeric values
            mark = float(mark)
            if mark < 0 or mark > 100:
                print("Invalid mark! Must be between 0 and 100.")
            else:
                self.marks_list.append(mark)
                print(f"Mark {mark} added successfully.")
        except ValueError:
            # Handle non-numeric input
            print("Invalid input! Please enter a numeric value.")

    def get_average(self):
        if not self.marks_list:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    def display_info(self):
        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks List:", self.marks_list)
        print("Average Marks:", self.get_average())


# Demonstration
student1 = Student("Aboli", 101)

# Add marks using user input
for i in range(5):
    mark_input = input(f"Enter mark for subject {i+1}: ")
    student1.add_mark(mark_input)

# Display student details
student1.display_info()
