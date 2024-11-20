#Program to enter users names and check if password is correct 

def passwordCheck(password):
    securePassword = ["!","?","$", "&"]
    if len(password) >= 8:
        passwordLength = True
    else:
        passwordLength = False
        print("Password Length is too short. Password should be larger or equal to 8") 

    for i in securePassword:
        if i in password:
            passwordSecurity = True
            break
        else:
            passwordSecurity = False
            print("Password Security is too low.")
            break

    if passwordLength and passwordSecurity :
        print("Password is accepted")
        return True 
    else:
        print("Password is not accepted")
        return False 

userNameDataBase = {
    "Homer" : "BeerisLife!",
    "Marge" : "Homeriswow!",
    "Bart"  : "MyDadisawesome$"
 }

userName = str(input("Enter user name : "))
userNamePassword = str(input("Enter password : "))
if passwordCheck(userNamePassword) is True:
    userNameDataBase[userName] = userNamePassword

print(userNameDataBase)




