import re
import math
import argparse


# Load common passwords listed in a text file- We will be comparing the chosen password against the common passwords
def load_common_passwords(filename="common_passwords.txt"):
    try:
        with open(filename, 'r') as file:
            return set(password.strip() for password in file.readlines())
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return set()


# Check the length of the password submitted by the user. Passwords longer than 8 characters tend to be stronger.
def check_length(password, min_length=8):
    return len(password) >= min_length


# Check the password for character variety- reducing the likelyhood of a brute force attack.
def check_variety(password):
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[\W_]', password)
    return all([has_upper, has_lower, has_digit, has_special])


# Check against common passwords
def check_common(password, common_passwords):
    return password not in common_passwords


# Check for dictionary words- Strong passwords shoudn't be easy to guess/find.
def check_dictionary(password, dictionary):
    return password.lower() not in dictionary


# Calculate entropy-The higher the entropy, the less likely it will be guessed. So its less predictable.
def calculate_entropy(password):
    pool = 0
    if re.search(r'[A-Z]', password):
        pool += 26
    if re.search(r'[a-z]', password):
        pool += 26
    if re.search(r'\d', password):
        pool += 10
    if re.search(r'[\W_]', password):
        pool += 32
    entropy = len(password) * math.log2(pool) if pool else 0
    return entropy


# Main function to check password strength
def check_password_strength(password, common_passwords):
    if not check_length(password):
        print("Password is too short.")
    elif not check_variety(password):
        print("Password lacks variety in characters.")
    elif not check_common(password, common_passwords):
        print("Password is too common.")
    else:
        entropy = calculate_entropy(password)
        print(f"Password is strong with an entropy of {entropy:.2f} bits.")


# CLI setup-Inclusion of error handling and prompt for user to input password
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Password Strength Checker")
    parser.add_argument("password", type=str, nargs='?', help="Password to check")
    args = parser.parse_args()

    if args.password:
        common_passwords = load_common_passwords()
        check_password_strength(args.password, common_passwords)
    else:
        password = input("Please enter a password to check: ")
        common_passwords = load_common_passwords()
        check_password_strength(password, common_passwords)
