import string

def check_password_strength(password):
    # Define sets of characters
    lowercase_letters = set(string.ascii_lowercase)
    uppercase_letters = set(string.ascii_uppercase)
    digits = set(string.digits)
    special_characters = set(string.punctuation)

    # Initialize criteria flags
    length_valid = len(password) >= 8
    has_lowercase = any(char in lowercase_letters for char in password)
    has_uppercase = any(char in uppercase_letters for char in password)
    has_digit = any(char in digits for char in password)
    has_special = any(char in special_characters for char in password)

    # Assess strength based on criteria
    strength = 0
    if length_valid:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def main():
    try:
        password = input("Enter your password to assess its strength: ").strip()
        strength = check_password_strength(password)

        print(f"Password strength score: {strength}/5")

        if strength < 3:
            print("Weak password. Consider making it stronger.")
        elif strength < 5:
            print("Moderate password. It could be stronger.")
        else:
            print("Strong password. Well done!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
