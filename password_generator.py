import random
import string

def generate_password(length=12, use_numbers=True, use_symbols=True):
    """
    Create a random password based on given options.

    Args:
        length (int): Desired length of the password (default: 12)
        use_numbers (bool): Whether to include numbers (default: True)
        use_symbols (bool): Whether to include special characters (default: True)

    Returns:
        str: The generated password
    """
    # Define character pools
    letters = string.ascii_letters
    numbers = string.digits if use_numbers else ""
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?" if use_symbols else ""

    # Merge allowed character sets
    char_pool = letters + numbers + special_chars
    if not char_pool:
        raise ValueError("Password must include at least one type of character.")

    # Ensure at least one character from each selected type
    password = []
    password.append(random.choice(letters))  # Always include at least one letter
    if use_numbers:
        password.append(random.choice(numbers))
    if use_symbols:
        password.append(random.choice(special_chars))

    # Fill the rest of the password with random choices
    password.extend(random.choice(char_pool) for _ in range(length - len(password)))

    # Shuffle to remove predictable patterns
    random.shuffle(password)

    return ''.join(password)

def main():
    """Quick demo of the password generator."""
    print("🔒 Password Generator 🔒\n")

    # Generate sample passwords
    print(f"Basic Password (8 chars, letters only):  {generate_password(8, False, False)}")
    print(f"Standard Password (12 chars, mixed):     {generate_password(12)}")
    print(f"Strong Password (16 chars, mixed):       {generate_password(16)}")

if __name__ == "__main__":
    main()