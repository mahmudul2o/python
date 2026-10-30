#Back end
#Homescreen
def homescreen():
    print("Homesceen")
    print("1. Login", "\n" "2. Sign in" "\n" "3. Delete a user")
    userinput = int(input('Select a number: '))
    if userinput == 1:
        loginpage()
    elif userinput == 2:
        signinpage()
    elif userinput == 3:
        usertodelete()
    else:
        print('Syntex erroe!')
#Login logic 
userdb = {}

# 1. Loading the Database
with open("file.txt", "r") as file:
    savedline = file.readlines()
    
    for line in savedline:
        cleanline = line.strip()
        # FIX: Only split the line if it actually contains a comma
        if ":" in cleanline: 
            username, password = cleanline.split(":")
            # Added .strip() to clean the password
            userdb[username] = password.strip()

#Sign in logic
def signinpage():
    print('Sign in page')
    newuser = input('Enter a new username: ')
    while newuser in userdb:
        newuser = input('User already exist. Please select a unique usarename: ')
        
    newpass = input('Enter a now password: ')
    userdb[newuser] = newpass
    #Saving the user and pass
    with open("file.txt", "a") as file:
        file.write(f"{newuser}:{newpass}\n")
    print("Congo! you are a user now")

# 2. Username Check
def loginpage():
    print("Login page")
    userlog = input("Enter your user name: ")
    attempts = 1

    while userlog not in userdb and attempts < 3:
        print(f"Wrong user. You have {3 - attempts} attempts left.")
        userlog = input("Enter your user name: ")
        attempts += 1  # Fixed typo

    # 3. Password Check
    if userlog in userdb:
        userpassword = input('Enter your password: ')
        attempt = 1 
    
    # FIX: Fixed indentation here
        while userpassword != userdb[userlog] and attempt < 3:
            print(f"Wrong password. You have {3 - attempt} left.")
            userpassword = input('Enter your password: ')
            attempt += 1
            
            if attempt == 3:
                homescreen()
        
    # FIX: Fixed indentation here
        if userpassword == userdb[userlog]:
            print('Login successful')
            print(f"Welcome {userlog}")
        else:
            print("Maximum attempts, please try again later.")
    else:
        print('User name not found')

#Delete a user
def usertodelete():
    print('Delete a user')
    usertodel = input('Enter the username you want to delete: ')
    while usertodel not in userdb and usertodel != "exit":
        usertodel = input(f"{usertodel} not found." "\n" "Enter the username you want to delete or type Exit to return into main screen: ")
    if usertodel == "exit":
        return
    elif usertodel in userdb:
        userpassword = input(f"Enter the password of {usertodel} : ")
        del userdb[usertodel]
        
        
        with open ("file.txt", "w") as file:
            for username, password in userdb.items():
                file.write(f"{usertodel}:{userpassword}\n")
            print(f"User {usertodel} has been deleted")

    else:
        print(f"{usertodel}is not a listed user")

#Front end
while True:
    print("\n-------------------------")
    homescreen()
