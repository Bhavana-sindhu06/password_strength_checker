import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1

    # Digit check
    if re.search(r"\d", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength evaluation
    if score <= 2:
        return "Weak Password ❌"
    elif score == 3:
        return "Medium Password ⚠️"
    elif score == 4:
        return "Strong Password ✅"
    else:
        return "Very Strong Password 🔐"


# User input
password = input("Enter your password: ")
print(check_password_strength(password))
