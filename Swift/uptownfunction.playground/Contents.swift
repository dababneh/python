import UIKit

var length = 5
var width = 10

var area = length * width

func calculateArea (length : Int , width: Int) -> Int {
    let area = length * width
    return area
}

print(calculateArea(length: calculateArea(length: 5, width: 3), width: 7))

