# Simple Password Strength Checker

This is a basic command-line tool designed to evaluate the strength of a password based on various criteria, including length, character variety, comparison against common passwords, and entropy calculation.

## Features
- **Length Check**: Ensures passwords meet a minimum length requirement (default is 8 characters).
- **Character Variety**: Verifies that the password contains a mix of uppercase letters, lowercase letters, numbers, and special characters.
- **Common Passwords**: Prevents the use of commonly known passwords.
- **Entropy Calculation**: Estimates the entropy (randomness) of the password, giving a rough indication of its strength.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/password_strength_checker.git
    cd password_strength_checker
    ```

2. **Ensure Python is Installed**:
    This script requires Python 3.6 or higher.

## Usage

You can run the script directly from the command line. There are two ways to provide a password:

### Option 1: Command-Line Argument

You can pass the password directly as an argument when running the script.

```bash
python password_checker.py "YourP@ssw0rd"
```

### Option 2: Run code & answer prompt

Run the without providing a password, it will prompt you to enter one

#### Finally:
You will be told whether your password has a problem and what that problem is or if its a strong password, you will be told how strong the password is.

### Next Steps:
- **Enhancements**: I could add a graphical interface, integrate it with web applications, or extend the criteria for password evaluation.

## License
This project is licensed under the MIT License.  
