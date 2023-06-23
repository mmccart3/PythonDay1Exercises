password = "Password1234"

password_length = len(password)

if password_length < 9:
    print("Password is too short")
else:
    print("Password length is OK")