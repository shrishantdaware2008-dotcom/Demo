def manage_marks():
    try:
        # 1. Take 5 subject marks as input from user
        marks = []
        for i in range(5):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            marks.append(mark)
        
        # 2. Calculate average, highest, lowest
        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)
        
        print("\n--- Results ---")
        print("Marks entered:", marks)
        print("Average marks:", average)
        print("Highest marks:", highest)
        print("Lowest marks:", lowest)
        
        # 3. Sort in descending order
        marks.sort(reverse=True)
        print("Marks in descending order:", marks)
    
    except ValueError:
        # Handle non-numeric input
        print("Invalid input! Please enter numeric values only.")

# Call the function
manage_marks()
