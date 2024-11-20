import UIKit

var middleName: String

struct person {
    let firstName : String
    let lastName : String
    let middleName : String?
    
    func printFullname() {
        print("\(firstName) \(String(describing: middleName)) \(lastName)")

}

var person1 = Person(person(firstName: "Jenna", lastName: "Dab", middleName: nil ))

person1.printFullname()
