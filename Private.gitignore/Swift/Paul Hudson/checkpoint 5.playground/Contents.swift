import UIKit

let luckyNumbers = [7, 4, 38, 21, 16, 15, 12, 33, 31, 49]

let _ = luckyNumbers
    .filter { !$0.isMultiple(of: 2) }   // filter out even numbers
    .sorted()                           // sort the odd numbers
    .map { print("\($0) is a lucky number.") }// map to strings
    

