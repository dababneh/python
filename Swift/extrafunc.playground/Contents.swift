import UIKit

func myFirstFunction() {
    print("Hahahaha")
    mySecondFunction()
}

func mySecondFunction() {
    print("Hahahaha Again")
}

myFirstFunction()

func getUserName () -> String {
    let userName = "Nick"
    return userName
}

let name = getUserName()

func checkIfUserIsPremium() -> Bool{
    return false
}

//-------------------------------
func showFirstScreen(){
    var userComplete: Bool = false
    var userProfileCreated: Bool = true
    let status = checkUserStatus(didComplete: userComplete, profileCretaed: userProfileCreated)
    
    if status == true {
        print("Yes")
    } else {
        print("No")
    }
}
func checkUserStatus(didComplete :Bool,profileCretaed : Bool) -> Bool {
    if didComplete && profileCretaed {
        return true
    }
    else {
        return false
    }
}

func doSomethingCool(someValue:Bool){
    
}
