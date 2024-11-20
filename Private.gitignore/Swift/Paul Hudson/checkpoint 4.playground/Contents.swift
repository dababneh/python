import UIKit
import Foundation


var greeting = "Hello, playground"

enum errorNumber : Error {
    case reallybad, noresult
}

func squareRoot (number : Int) throws -> Int {
    if number < 1 || number > 10000 {
        throw errorNumber.reallybad
    }
    
    for i in 1...100 where i*i == number {
       return i
    }
    return 0
}


do {
    try print(squareRoot(number: 100)) }
catch errorNumber.reallybad {
    print("Hell no to the no no no no no ")
}

enum weather {
    case sun, rain, wind, snow, unknown
}

var forecast = weather.rain

switch forecast {
case .sun:
    print("It should be a nice day.")
case .rain:
    print("Pack an umbrella.")
case .wind:
    print("Wear something warm")
case .snow:
    print("School is cancelled.")
case .unknown:
    print("Our forecast generator is broken!")
}

let input = readLine()
print(input ?? "Error")

