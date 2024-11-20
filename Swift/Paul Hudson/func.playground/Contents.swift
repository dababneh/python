import UIKit

func findmeanumber(number : Int) -> Int {
    var numbers = Int.random(in: 1...100)
    return numbers * 5 + number

}

print(findmeanumber(number: 10))

func multiples(number : Int){
    for i in 5...19 {
        print("\(i) X \(number) = \(i*number)")
    }
}

multiples(number: 99)


enum passworderror : Error {
    case good, bad
}

func checkPassword(_ password : String) throws -> String {
    if password.count < 5 {
        throw passworderror.bad
    }
    if password == "12345" {
        throw passworderror.good
    }
    
    if password.count < 8 {
        print("yay")
    }
    return "yay"
    
}

do {
    try checkPassword("123")}
    catch {
        print("oh no ")
    }

