import math

def unique_words_analysis():
    try:
        # 1. Take sentence input
        sentence = input("Enter a sentence: ").strip()
        
        if not sentence:
            print("Empty sentence provided.")
            return
        
        # 2. Extract unique words using set
        words = sentence.split()
        unique_words = set(words)
        
        # 3. Print unique words in sorted order
        sorted_words = sorted(unique_words)
        print("\nUnique words (sorted):", sorted_words)
        
        # 4. Use math module to raise count of unique words to power 2
        count = len(unique_words)
        result = math.pow(count, 2)
        print(f"Total unique words: {count}")
        print(f"{count} raised to power 2 = {result}")
    
    except Exception as e:
        print("An error occurred:", e)

# Run the program
unique_words_analysis()
