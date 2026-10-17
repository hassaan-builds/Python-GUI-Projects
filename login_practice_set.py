#correct email is hassaan@gmail.com
#correct password is "1234"
correct_email="hassaan@gmail.com"
correct_password="1234"
email=input("Enter your email:")
if "@" in email:
    password=input("Enter your password:")

    if email==correct_email and password==correct_password:
            print("login")
    elif email==correct_email and password !=correct_password:
            print("password is wronge")
            password=input("again enter your password:")

            if password==correct_password:
                print("finally correct password")
                print("Welcome")
            else:
                print("still incorrect")

    else:
            print("incorrect credential")
else:
    print("Email formate is wronge")












print(".................Improve code..................")
from getpass import getpass

# Correct credentials
correct_email = "hassaan@gmail.com"
correct_password = "1234"

# Get email
email = input("Enter your email: ").strip()

# Check email format
if "@" not in email or "." not in email:
    print("Email format is wrong")

# Check email
elif email != correct_email:
    print("Incorrect email")

# Email is correct
else:
    password = getpass("Enter your password: ")

    # Check password
    if password == correct_password:
        print("Login successful!")
        print("Welcome Hassan!")

    else:
        print("Wrong password")
        password = getpass("Enter your password again: ")

        # Second password attempt
        if password == correct_password:
            print("Login successful!")
            print("Welcome Hassan!")

        else:
            print("Still incorrect!")
            print("Login failed!")
