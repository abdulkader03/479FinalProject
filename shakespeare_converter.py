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
    "shalt": "shall",
    "thee": "you",
    "tis": "it is",
    "hast": "have",
    "wilt": "will",
    "hence": "away",
    "wherefore": "why",
    "ere": "before",
    "oft": "often",
    "ne'er": "never",
    "white": "fair",
    "dinner": "supper",
    "nay": "no",
    "perchance": "perhaps",
    "oftentimes": "often",
    "ofttimes": "often",
    "fain": "gladly",
    "anon": "soon",
    "giveth": "give",
    "in": "amidst",
    "receiveth": "receive",
    "maketh": "make",
    "breaketh": "break",
    "goeth": "go",
    "cometh": "come",
    "knoweth": "know",
    "speaketh": "speak",
    "sitteth": "sit",
    "riseth": "rise",
    "eateth": "eat",
    "drinketh": "drink",
    "believeth": "believe",
    "followeth": "follow",
    "dog": "hound",
    "the": "the",
    "boat": "vessel",
    "small": "low",
    "horse": "steed",
    "brown": "chestnut",
    "standing": "standeth",
    "on top": "atop",
    "field": "meadow",
    # Add more mappings as needed
}

# Function to convert Shakespearean text to modern English
def shakespeare_to_modern(text):
    # Make sure text is a string
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

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