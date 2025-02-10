import random
import string

def generate_password(length=12, include_numbers=True, include_symbols=True):
    """
    Generate a secure password with customizable options.
    
    Args:
        length (int): Length of the password (default: 12)
        include_numbers (bool): Include numbers in password (default: True)
        include_symbols (bool): Include special characters (default: True)
    
    Returns:
        str: Generated password
    """
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits if include_numbers else ""
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" if include_symbols else ""
    
    # Combine all allowed characters
    all_characters = letters + digits + symbols
    
    # Ensure password contains at least one character from each selected type
    password = [
        random.choice(letters),  # Ensure at least one letter
        random.choice(digits) if include_numbers else "",
        random.choice(symbols) if include_symbols else ""
    ]
    
    # Fill the rest of the password
    remaining_length = length - sum(len(x) for x in password)
    password.extend(random.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle the password characters
    password_list = list(''.join(password))
    random.shuffle(password_list)
    
    return ''.join(password_list)

def main():
    """
    Main function to demonstrate password generation with different options.
    """
    print("Password Generator\n")
    
    # Generate different types of passwords
    simple_pass = generate_password(length=8, include_numbers=False, include_symbols=False)
    standard_pass = generate_password(length=12)
    strong_pass = generate_password(length=16)
    
    print(f"Simple Password (8 chars, letters only): {simple_pass}")
    print(f"Standard Password (12 chars, all chars): {standard_pass}")
    print(f"Strong Password (16 chars, all chars): {strong_pass}")

if __name__ == "__main__":
    main()