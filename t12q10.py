import math

# --- Basic Arithmetic Functions ---
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None

# --- Scientific Calculations ---
def scientific_calculations():
    try:
        num = float(input("Enter a number: "))
        print("Square root:", math.sqrt(num))
        print("Factorial:", math.factorial(int(num)))
        print("Ceiling:", math.ceil(num))
        print("Floor:", math.floor(num))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print("Error:", e)

# --- Data Manager (Session Storage) ---
session_data = []

def store_result(result):
    if result is not None:
        session_data.append(result)
        print("Result stored in session.")

def view_session():
    if session_data:
        print("Session Data:", session_data)
        print("Sum of session data:", sum(session_data))
        print("Average of session data:", sum(session_data)/len(session_data))
    else:
        print("No data stored in session yet.")

# --- Main Menu ---
def main():
    while True:
        print("\n--- Smart Calculator & Data Manager ---")
        print("1. Basic Arithmetic")
        print("2. Scientific Calculations")
        print("3. View Session Data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Choose operation: + - * /")
                op = input("Operation: ")

                if op == "+":
                    result = add(a, b)
                elif op == "-":
                    result = subtract(a, b)
                elif op == "*":
                    result = multiply(a, b)
                elif op == "/":
                    result = divide(a, b)
                else:
                    print("Invalid operation!")
                    result = None

                if result is not None:
                    print("Result:", result)
                    store_result(result)

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == "2":
            scientific_calculations()

        elif choice == "3":
            view_session()

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the program
main()
