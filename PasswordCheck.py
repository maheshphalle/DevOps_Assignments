# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 
# Implement a Python function called check_password_strength that takes a password string as input.
# The function should check the password against the following criteria:
# Minimum length: The password should be at least 8 characters long.
# Contains both uppercase and lowercase letters.
# Contains at least one digit (0-9).
# Contains at least one special character (e.g., !, @, #, $, %).
# The function should return a boolean value indicating whether the password meets the criteria.
# Write a script that takes user input for a password and calls the check_password_strength function to validate it.
# Provide appropriate feedback to the user based on the strength of the password.  


def check_password_strength(password):
    # Check for minimum length
    if len(password) < 8:
        print("Password should have more than 8 characters.")
        return False, "Password should have more than 8 characters."

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        print("Password should have at least one lowercase letter.")
        return False, "Password should have at least one lowercase letter."

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter.")
        return False, "Password should contain at least one uppercase letter."

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        print("Password should have at least one digit.")
        return False, "Password should have at least one digit."

    # Check for at least one special character
    spl_char = "!@#$%^&*()-=+~|\'<>?"
    if not any(char in spl_char for char in password):
        print("Password must contain at least one special character.")
        return False, "Password must contain at least one special character."

    print("Password meets all requirements.")
    return True, "Password meets all requirements."

def main():
    password = input("Enter a password to check its strength: ")
    is_strong, message = check_password_strength(password)
    
    if is_strong:
        print("Correct", message)
    else:
        print("Wrong", message)


if __name__ == "__main__":
    main()