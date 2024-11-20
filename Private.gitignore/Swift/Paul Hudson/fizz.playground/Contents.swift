import UIKit
import Foundation

var testData = [
    1, // Expected Output: "1"
    3, // Expected Output: "Fizz"
    5, // Expected Output: "Buzz"
    15, // Expected Output: "FizzBuzz"
    86 // Expected Output: "86"
]

func fizzBuzz(_ number: Int) -> String {
    var result : String
    if number.isMultiple(of: 3) && number.isMultiple(of: 5){
        result = "FizzBuzz"
    } else if number.isMultiple(of: 3){
        result = "Fizz"
    } else if number.isMultiple(of: 5){
        result = "Buzz"
    } else {
        result = String(number)
    }
    return result
}

for number in testData {
    print(fizzBuzz(number))
}
