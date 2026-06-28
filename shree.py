def analyze_string(s):
    if not s:  # handle empty string case
        print("Empty string provided.")
        return
    
    # 1. Print length
    print("Length of string:", len(s))
    
    # 2. Print reverse using slicing
    print("Reversed string:", s[::-1])
    
    # 3. Count vowels (case-insensitive)
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)
    
    # 4. Print each character with positive and negative index
    for i in range(len(s)):
        print(f"Character: {s[i]} | Positive index: {i} | Negative index: {-len(s)+i}")

# Call the function with user input
user_input = input("Enter a string: ")
analyze_string(user_input)
