import re

def contains_alphabets(input_string):
    cleaned_string = input_string.replace(' ', '_')
    # Remove special characters and numbers
    cleaned_string = re.sub(r'[^a-zA-Z_]', '', cleaned_string)

    # Check if the cleaned string contains alphabets
    return any(char.isalpha() for char in cleaned_string),cleaned_string

# Example usage:
input_str = "  "
result,clean_String = contains_alphabets(input_str)

if not result:
    print(f"The cleaned string '{clean_String}' does not contain alphabets.")
else:
    print(f"The cleaned string '{clean_String}' contains alphabets.")
