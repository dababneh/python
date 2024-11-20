import UIKit

var message = "Hello, World"
print(message)
var k = 1

    for i in message {
        print (k, ":", i)
        k += 1
        if k == 10 {
            break
    }
}

var message1 : String = "I am the wooooo"
    print (message1)

var fullName = "Jamil Dababneh"
var amessage : String = "hey there"

var messageA = "Adriana Keropi"

for i in messageA {
    print (i)
}

let firstName = "Jenna"
let lastName = "Smith"

fullName = firstName + " " + lastName
print(fullName) //wow

var age = 20
var newMessage = "Hi, my name is \(firstName) and I am \(age) years old"
print(newMessage)

newMessage.append(". And I like scary clowns")
print(newMessage)

var average : Int

average = 100

newMessage.append("\(average)")

print(newMessage)

