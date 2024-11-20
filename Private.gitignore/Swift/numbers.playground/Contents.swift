import UIKit

var age = 15 // Integer
var price = 10.99 // Double
var aPrice : Float = 10.99
var personAge : Int = 15
var thePrice : Double = 10.99

var length = 10
var widgth = 5
let area = length * widgth // mult

print (area)

var health = 100
var posionDamage = 15
health = health - posionDamage

print(health)

health -= posionDamage

print(health)

var potion = 20
health += potion

print(health)

var students = 30
var treats = 500

let treatPerStudent  = Double (treats % students) // Division

print(treatPerStudent)

var tLength : Double = 10
var tWidth : Double = 5

let areaTriangle = sqrt(pow(tLength, 2) + pow(tWidth, 2))
print(Float(areaTriangle))

var quantity : Int = 5
var productPrice : Double = 10.99

var cost = Double(quantity) * productPrice

var nums = [1,2,3,4,5]

print(nums.count)
var count : Int = 0

for i in nums {
    count += i
}

print(count)
var list1 : [Int] = []
for i in nums {
    if i%2 == 0 {
        print("Yes \(i)")
    }else{
        print("No \(i)")
        list1.append(i)
    }
}
    print(list1)


