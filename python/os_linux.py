import os
import subprocess

def new_user():
    confirm ="N"
    while confirm != "Y":
        userName = input("Enter the name of the user to add")
        print("Use the username'" + userName + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser" + userName)
    
new_user()

def remove_user(): 
    confirm = "N" 
    while confirm != "Y": 
        username = input("Enter the name of the user to remove: ") 
        print("Remove the user : '" + username + "'? (Y/N)") 
        confirm = input().upper()
    os.system("sudo userdel -r " + username)

#Activity: Adding a user to a group (1)
def add_user_to_group(): 
    username = input("Enter the name of the user that you want to add to a group: ") 
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0] 
    print("Enter a list of groups to add the user to") 
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3") 
    print("The available groups are:\r\n " + output) 
    chosenGroups = str(input("Groups: "))

#Activity: Adding a user to a group (2)
