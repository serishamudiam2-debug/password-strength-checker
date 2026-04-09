import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character checks
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength levels
    if score <= 2:
        return "Weak ❌"
    elif score <= 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

# Run program
password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)