import UIKit

var employee1salary = 45000.0
var employee2salary = 54000.0
var employee3salary = 100000.0
var employee4salary = 20000.0

var employeeSalaries = [45000.0 , 54000.0, 100000.0, 20000.0]
print(employeeSalaries)
employeeSalaries.append(39000.34)

print(employeeSalaries.count)
employeeSalaries.remove(at: 1)
print(employeeSalaries.count)
var students = [String]()
print(students.count)
var students2 = [String]()
students2.append("Jamil Dababneh")
print(students2)


struct appData {
    var version = "wow"
}

var jamil = appData()
jamil.version = "hey"
print(appData().version)
print(jamil.version)


enum weather {
    case sun, rain, hot, cold, wow
}

let todaysWeather : weather = .wow

switch todaysWeather {
case .sun:
    print("Its sunny")
case .rain:
    print("Its rainy")
case .hot:
    print("Its hot")
case .cold:
    print("Its cold")
default :
    print("Its i dont know")
    
}

let numbers: [Int] = [2,7,9,10]
let target : Int = 9

for x in 0...numbers.count{
    for y in 1...numbers.count{
        if numbers[x] + numbers[y] == target{
            print(x,y)
        }
    }
}




