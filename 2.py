def char_count(input_string):
    # Initialize an empty dictionary to store character counts
    count_dict = {}
    
    # Iterate over each character in the string
    for char in input_string:
        if char in count_dict:
            # Increment the count if the character is already in the dictionary
            count_dict[char] += 1
        else:
            # Add the character to the dictionary with a count of 1
            count_dict[char] = 1
    
    # Print the character counts
    for char, count in count_dict.items():
        print(f"'{char}': {count}")

# Take user input
input_string = input("Enter a string: ")

# Call the function to count characters
char_count(input_string)

