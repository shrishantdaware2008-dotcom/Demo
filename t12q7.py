# Lambda function to calculate square
square = lambda x: x * x

def generate_squares():
    try:
        # 1. Generate numbers from 1 to 20
        numbers = range(1, 21)
        
        # 2. Store squares in a list using lambda
        squares = [square(num) for num in numbers]
        print("All squares:", squares)
        
        # 3. Print only even squares
        even_squares = [sq for sq in squares if sq % 2 == 0]
        print("Even squares:", even_squares)
    
    except Exception as e:
        print("An error occurred:", e)

# Call the function
generate_squares()
