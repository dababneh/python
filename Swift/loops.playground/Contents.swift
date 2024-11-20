import UIKit

var employee1Salary = 45000.0
var employee2Salary = 54000.0
var employee3Salary = 100000.0
var employee4Salary = 20000.0

employee1Salary = employee1Salary + (employee1Salary * 0.10)
employee2Salary = employee2Salary + (employee2Salary * 0.10)

var Salaries: [Double] = [45000.0,54000.0,100000.0, 20000.0,45000.0,54000.0,100000.0, 20000.0,45000.0,54000.0,100000.0, 20000.0,45000.0,54000.0,100000.0, 20000.0,45000.0,54000.0,100000.0, 20000.0,45000.0,54000.0,100000.0, 20000.0]

Salaries[0] = Salaries[0] + (Salaries[0] * 0.10)

var x = 0
var y : Double = 0
var salaries1 = [Double]()
repeat {
    y = Salaries[x] + (Salaries[x] * 0.10)
    salaries1.insert(y, at: x)
    x += 1
} while (x < Salaries.count)
print(Salaries)
print(".    .    .    .    .    .    .    .")
print(salaries1)

var z = 0
var q : Double = 0
for i in 0..<Salaries.count{
    q = Salaries[i] + (Salaries[i] * 0.10)
    salaries1.insert(q, at: x)
}
print(salaries1)

for Salary in Salaries {
    print("Salary : \(Salary)")
}
