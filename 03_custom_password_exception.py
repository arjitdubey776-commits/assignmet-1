class WeakPasswordError(Exception):
    pass

password = input("Enter a password: ")

try:
    if len(password) < 8:
        raise WeakPasswordError("Password must contain at least 8 characters")

    print("Password accepted")
except WeakPasswordError as error:
    print(error)
