correct_password = "python123"

# TODO: Your code here
login_successful = False
attempts_used = 0

for i in range(3):
    attempts_used = i + 1  # Track the current attempt number
    
    # Get password from user
    user_input = input("Enter password: ")
    
    # Check if the password is correct
    if user_input == correct_password:
        login_successful = True
        print("Access granted!")
        break  # Stop the loop immediately
    else:
        # Only print 'denied' if it's not the last attempt
        if attempts_used < 3:
            print("Access denied. Try again.")
        else:
            print("Access denied. No attempts remaining.")

print(login_successful)
print(attempts_used)