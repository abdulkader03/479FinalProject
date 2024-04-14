import re

# Define a dictionary to map Shakespearean terms to modern English
shakespeare_to_english = {
    "thou": "you",
    "thy": "your",
    "thine": "yours",
    "hath": "has",
    "doth": "does",
    "art": "are",
    "mayst": "may",
    "dost": "do",
    # Add more mappings as needed
}

# Function to convert Shakespearean text to modern English
def shakespeare_to_modern(text):
    # Use regular expressions to find and replace Shakespearean terms
    for shakespeare_word, modern_word in shakespeare_to_english.items():
        # Use word boundary to avoid partial matches
        text = re.sub(r'\b{}\b'.format(shakespeare_word), modern_word, text, flags=re.IGNORECASE)
    return text

# Function to read text from a file and convert it to modern English
def convert_file(filename):
    with open(filename, 'r') as file:
        shakespeare_text = file.read()
    modern_text = shakespeare_to_modern(shakespeare_text)
    return modern_text

# Text file example input
input_file = "shakespeare_input.txt"
modern_text = convert_file(input_file)
print("Shakespearean text:")
print(modern_text)
