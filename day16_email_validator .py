email = input("Enter your email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")