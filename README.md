# Password Strength Checker

This is a simple password strength checker written in Python. The program analyzes a password’s length, character diversity (uppercase, lowercase, digits, special characters), and checks if the password appears in a common password list to provide a strength rating.

## Features

- Checks for uppercase, lowercase, digits, and special characters in the password.
- Evaluates password length and assigns score based on length thresholds.
- Verifies if the password exists in a common passwords list (`password.txt`).
- Outputs a strength label: weak, ok, fine, or strong.

## Usage

1. Make sure you have Python installed.
2. Ensure a `password.txt` file is present in the same directory (with commonly used passwords, one per line).
3. Run the script:
    ```
    python PSC.PY
    ```
4. Enter the password to check when prompted.
5. The program will print the strength of your password, along with score details.

## Credits

This project was created for learning purposes by following a YouTube tutorial on password strength checkers. Additional modifications and understanding were applied during the implementation.[NeuralNine]
