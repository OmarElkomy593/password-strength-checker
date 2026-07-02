def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False


def check_uppercase(password):
    for c in password:
        if c.isupper():
            return True
    return False


def check_lowercase(password):
    for c in password:
        if c.islower():
            return True
    return False


def check_digit(password):
    for c in password:
        if c.isdigit():
            return True
    return False


def check_special(password):
    for c in password:
        if not c.isalnum():
            return True
    return False



for attempt in range(3):
    attempt += 1
    LINE = "=" * 30
    print(f"Attempts: {attempt}/3")
    password = input("Enter your password: ")
    print("Checking password...")
    length_valid = check_length(password)
    uppercase_valid = check_uppercase(password)
    lowercase_valid = check_lowercase(password)
    digit_valid = check_digit(password)
    special_valid = check_special(password)
    if (
        length_valid
        and uppercase_valid
        and lowercase_valid
        and digit_valid
        and special_valid
    ):
        print(LINE)
        print("Password Accepted:")
        print("Score: 5/5")
        print(LINE)
        break
    else:
        symbols = ["✖", "✔"]
        print(LINE)
        print("Password Strength Report:")
        print("Length :", symbols[length_valid])
        print("Uppercase :", symbols[uppercase_valid])
        print("Lowercase :", symbols[lowercase_valid])
        print("Digit :", symbols[digit_valid])
        print("Special Character :", symbols[special_valid])
        print(
            f"Score: {length_valid + uppercase_valid + lowercase_valid + digit_valid + special_valid}/5"
        )
        print(LINE)
        if attempt == 3:
            print(LINE)
            print("Maximum attempts reached. Exiting program.")
            print(LINE)
            break
        print("Invalid password. Please try again.")