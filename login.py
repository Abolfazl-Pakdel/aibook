# creat login with python
 
#!/bin/bash

echo "======================="
echo "       Login Page      "
echo "======================="

read -p "Username: " username
read -sp "Password: " password
echo

# Demo credentials
correct_user="admin"
correct_pass="password123"

if [[ "$username" == "$correct_user" && "$password" == "$correct_pass" ]]; then
    echo "Login successful. Welcome, $username!"
else
    echo "Login failed. Invalid credentials."
fi