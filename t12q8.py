class Employee:
    def __init__(self, emp_id, name, details):
        # details is a tuple (department, salary)
        self.emp_id = emp_id
        self.name = name
        self.details = details

    def show_details(self):
        dept, salary = self.details
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {dept}, Salary: {salary}")


def main():
    try:
        # Dictionary with emp_id as key and Employee object as value
        employees = {}

        # Add 3 employees
        employees[101] = Employee(101, "Aboli", ("HR", 50000))
        employees[102] = Employee(102, "Rohan", ("IT", 60000))
        employees[103] = Employee(103, "Sneha", ("Finance", 55000))

        # Display all employees using loop
        print("\n--- Employee Details ---")
        for emp_id, emp_obj in employees.items():
            emp_obj.show_details()

    except Exception as e:
        print("An error occurred:", e)


# Run the program
main()
