import os 
import sys
import getpass

print("\nWelcome to the fancy system")
password = "Jamil1234"
for i in range(1,4):
    print("Please enter your password: \n")
    pass1 = getpass.getpass()
    if pass1 == password:
        print("\nLog in was successful.\n")
    else:
        print("\nYou have used " +str(i)+ "/3 attempts\n")