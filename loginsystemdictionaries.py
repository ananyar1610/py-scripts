

#implement a basic login systm using python dictionaries
''' Tasks:
- Store username password paris in a dictionaey
- Allow users to login by entering credentials
- Validate inpts and handle incorrect attempts (max 3 attempts)



'''
num=int(input("Enter number of username and password pairs:"))
username_pairs={}


for i in range(num):
 usernames=input("Enter username:")
 passwords=input("Enter password:")
 username_pairs[usernames]=passwords
print(username_pairs)

def login():
  attempts=0

  while(attempts<3):
    username=input("Enter username:")
    password=input("Enter password:")
    if username in username_pairs:
      if password in username_pairs[username]:
        print("'You've logged in succesfully.")
        print("Thank you for using our service.")
        break

      else:
        print("Invalid username or password. Please try again.")
        attempts+=1


      if attempts==3:
        print("Too many wrong attempts!")
        break

login_consent=input("Do you want to Login? Type 'yes' or 'no'").lower()

if login_consent=='yes':
  login()
else:
  print("Thank you for using our service.")

