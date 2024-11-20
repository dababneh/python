import UIKit

class employee {
    let bagde : Int
    let name : String
    
    init(bagde: Int, name: String) {
        self.bagde = bagde
        self.name = name
    }
    
    func printEmployeeInfo(){
        print("\(name) has been working hard and his bagde number is \(bagde)")
    }
}

let employee1 = employee(bagde: 515254, name: "Jamil Dababneh")
employee1.printEmployeeInfo()

