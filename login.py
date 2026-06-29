# creat login with python

import getpass

def check_credentials(username, password):
    # For demo purposes, using a hardcoded username and password.
    # In a real app, replace with proper user db/check.
    valid_username = "admin"
    valid_password = "password123"
    return username == valid_username and password == valid_password

def login():
    print("=== Login Page ===")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if check_credentials(username, password):
        print("Login successful! Welcome,", username)
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

if __name__ == "__main__":
    # Loop until successful login
    while not login():
        pass