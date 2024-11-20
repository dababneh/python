import re

def compute_if_valid(phrase: str):
    # Define a regular expression to match valid mathematical characters
    valid_expression = r'^[\d\s\+\-\*/\(\)]+$'
    
    # Remove any spaces from the input phrase
    phrase = phrase.replace(" ", "")
    
    # Check if the phrase matches the valid pattern for mathematical expressions
    if not re.match(valid_expression, phrase):
        return "Invalid input: Not a mathematical expression"
    
    # Try to compute the phrase and catch any errors
    try:
        result = eval(phrase)  # Evaluate the expression safely
        return result
    except (SyntaxError, ZeroDivisionError, NameError):
        return "Error: Could not compute the expression"

# Examples:
phrases = [
    "2 + 3 * (5 - 1)",
    "Hello + 5",
    "(2 + 5) / 0",
    "10 * (3 + 4)",
]

for phrase in phrases:
    print(f"'{phrase}' result: {compute_if_valid(phrase)}")
