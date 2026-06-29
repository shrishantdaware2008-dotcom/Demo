import random
import math

def process_numbers():
    try:
        # 1. Take 10 numbers as input
        numbers = []
        for i in range(10):
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
        
        # 2. Store unique numbers in a set
        unique_set = set(numbers)
        print("\nUnique numbers (set):", unique_set)
        
        # 3. Convert set into tuple
        num_tuple = tuple(unique_set)
        print("Tuple from set:", num_tuple)
        
        # 4. Pick 3 random numbers from tuple
        if len(num_tuple) >= 3:
            random_nums = random.sample(num_tuple, 3)
            print("3 Random numbers from tuple:", random_nums)
        else:
            print("Not enough unique numbers to pick 3.")
        
        # 5. Square root of sum of tuple elements
        total_sum = sum(num_tuple)
        print("Sum of tuple elements:", total_sum)
        print("Square root of sum:", math.sqrt(total_sum))
    
    except ValueError:
        print("Invalid input! Please enter integers only.")
    except Exception as e:
        print("An error occurred:", e)

# Call the function
process_numbers()
