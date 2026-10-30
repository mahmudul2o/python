def signin_screen():
    print("==============")
    print(" Sign in page ")
    print("==============")
def login_screen():
    print("================")
    print("   Login Page   ")
    print("================")
signin_screen()
user = input("Enter a user name: ")
password = input("Enter a password: ")
login_screen()
user_logon = input("Enter your user name: ")
if user_logon == user:
    attempt = 1
    user_password = input("Enter your password: ")
    while user_password != password and attempt < 3:
        print(f"Wrong password, you have {3 - attempt} attemps left.")
        user_password = input("Enter your password: ")
        attempt += 1
    if user_password == password:
        print("Login succesful!")
        print(f"Welcome {user}")
    else:
        print("You have reached maximum attempts.")
else:
    print("User not found!")

