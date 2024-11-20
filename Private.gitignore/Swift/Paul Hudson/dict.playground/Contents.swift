import UIKit

let contactInfo = [
    "name" : "Jamil",
    "Age" : "30"
    
]

print(contactInfo["name", default: "Not sure"])

var height = [String : Int ]()
height["Jamil"] = 10
print(height.keys)


var actors = Set<String>()
actors.insert("Jamil989")
actors.insert("Jamil2")
print(actors)

print(actors.sorted())

enum weekday {
    case saturday
    case monday
}

var day = weekday.saturday
day = .monday


var userNameDataBase = [
    "Homer" : 1,
    "Marge" : 5,
    "Bart"  : 9,
    "Homer" : 1,
 ]

print(userNameDataBase)

var wow = [String]()

for (name, something) in userNameDataBase{
    if wow .contains(name){
        userNameDataBase[name]! += 1
    }else{
        userNameDataBase[name] = 1
        }
    
    }
print(wow)


