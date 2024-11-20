import os 
import time 


os.chdir('/users/master/Desktop')
f = open("Pythonfile.txt","w+")
for i in range (5):
    k = input("Please enter a name: ")
    f.write("First name is : " +k+ "\n")
f = open("Pythonfile.txt" , "r")
for line in f:
    if "Jamil" in line:
        print("True")
    else: 
        print("false")
print("This is the content of the file : \n")
f = open("Pythonfile.txt" , "r")
print(f.readlines())
print(os.getcwd())
f.close()

