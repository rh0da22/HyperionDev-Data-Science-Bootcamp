import random

accounts = {}
current_balance = {}

def read_data():
    
    with open('Safe Bank Users.txt', 'r') as file:
    
        for lines in file:
            data = lines.strip().split(',')
            
            email = data[0]
            passw = data[1]

            accounts[email] = passw
            current_balance[email] = random.randint(100, 999999)

read_data()         

def check_bal(user_email):
    return f"Your current balance is £{current_balance[user_email]}"

def transfer_funds(sender_email, recipient_email, amount): 
    
    if sender_email not in accounts:
        print(f"This email [{sender_email}] is not registered.")
        return "TRANSFER FAILED."
    
    if amount > current_balance[sender_email]:
        print("Insufficient funds. Transfer has failed.")
        return "TRANSFER FAILED."

    current_balance[sender_email] -= amount

    print(f"Transfer successful! £{amount} has been transferred from {sender_email} to {recipient_email}.")
    print(f"Your new balance is £{current_balance[sender_email]}")

    return " "

def deposit(user_email, amount):
    if user_email not in accounts:
        print("This email is not registered.")
        return "DEPOSIT FAILED."
    
    current_balance[user_email] += amount
    print(f"Deposit successful! £{amount} has been deposited into {user_email}'s account.")
    print(f"Your current balalance is now {current_balance[user_email]}")
    
    return " "

def withdraw(user_email, amount):
    if user_email not in accounts:
        print("This email is not registered.")
        return "WITHDRAWAL FAILED."
    
    if amount > current_balance[user_email]:
        print(f"You have insufficient funds. Withdrawal failed.")
        return "WITHDRAWAL FAILED."
    
    current_balance[user_email] -= amount
    print(f"Withdrawal successful! £{amount} has been withdrawn from {user_email}'s account.")
    print(f"Your new balance is: £{current_balance[user_email]}")
    
    return " "


# This section of the code asks the user to either log in or register an account.

print("Hello, welcome to SafeBank. Would you like to log in or register an account?")
option = int(input("Enter 1 to log in or 2 to register: "))

email_attempts = 0

while True:
    if option==1:
        user_email = input("Enter your email: ")
        while user_email not in accounts.keys():
            email_attempts += 1
            print("This email is not recognised, please try again.")

            if email_attempts >= 3:
                print("Are you new here? Let's register a new account.")
                option = 2
                break

            user_email = input("Enter your email: ")

        if user_email in accounts:
            pw_attempts = 0
            user_password = input("Enter your password: ")
            while user_password != accounts[user_email]:
                pw_attempts += 1
                print(f"This password is incorrect, please try again. Attempt {pw_attempts} of 3.")

                if pw_attempts >= 3:
                    print("You have reached the maximum number of password attempts. Please try again later.")
                    exit()

                user_password = input("Enter your password: ")
            
            if user_password == accounts[user_email]:
                print("Login Successful!")
                break

    elif option==2:
        new_user_name = input("Enter your name: ")
        
        while True:
            new_user_email = input("Enter your email: ")

            if '@' in new_user_email and '.' in new_user_email:
                break
            else:
                print("Invalid Email, try again!")

        while new_user_email in accounts:
            print("This email is already registered. Please choose another: ")
            new_user_email = input("Enter your email: ")

        new_user_pw = input("Enter your password: ")
        confirm_pw = input("Enter your password again to confirm: ")

        while new_user_pw != confirm_pw:
            print("The passwords do not match. Please try again")
            confirm_pw = input("Enter your password again to confirm: ")
        
        print(f"Your new account with SafeBank has been created! Welcome {new_user_name}!")
        accounts[new_user_email] = new_user_pw
        current_balance[new_user_email] = random.randint(100, 999999)

        with open('Safe Bank Users.txt', 'a') as file:
            file.write(f"{new_user_email},{new_user_pw}\n")
        
        break

    else:
        print("Invalid option. Please enter 1 to log in or 2 to register.")
        break


while True: 
    print("What would you like to do today? ")
    print("""
          0. Log out
          1. Check your current balance
          2. Transfer funds 
          3. Deposit money
          4. Withdraw money 
          """)

    choice = int(input("Make a selection from the options above (enter 1, 2, 3, 4, or 0): " ))

    if choice == 1:
        print(check_bal(user_email))

    elif choice == 2:
        user = input("Enter your email: ")
        recipient = input("Enter the recipient's email: ")
        amount = int(input("Enter the amount you want to send: "))
        print(transfer_funds(user, recipient, amount))

    elif choice == 3:
        user = input("Enter your email: ")
        amount = int(input("Enter the amount you want to deposit: "))
        print(deposit(user, amount))


    elif choice == 4:
        user = input("Enter your email: ")
        amount = int(input("Enter the amount you want to withdraw: "))
        print(withdraw(user, amount))

    elif choice == 0:
        print("You are now logged out. Goodbye.")
        break

    else:
        print("Invalid choice, please try again.")

    answer = input("Would you like to do anything else? 'Y' for yes or anything else for no:").upper()
    if answer != "Y":
        print("Thank you for banking with SafeBank. Goodbye.")
        break