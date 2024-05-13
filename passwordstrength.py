import re

def assess_password_strength(password):
    # Initialize variables to track criteria
    length = len(password)
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special_char = False

    # Define regex patterns for special characters and numbers
    special_char_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    number_pattern = re.compile(r'[0-9]')

    # Check each character of the password
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True
        elif special_char_pattern.search(char):
            has_special_char = True

    # Assess strength based on criteria
    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_number:
        strength += 1
    if has_special_char:
        strength += 1

    return strength

def feedback(strength):
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    elif strength >= 2:
        return "Moderate"
    elif strength >= 1:
        return "Weak"
    else:
        return "Very Weak"

# Example usage
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", feedback(strength))
