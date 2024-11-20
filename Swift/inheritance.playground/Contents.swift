import UIKit

class Vehicle {
    var tires = 4
    var make : String?
    var model : String?
    var currentSpeed: Double = 0
    
    init(){
        print("I Am the Parent")
    }
    
    func drive(speedIncrease: Double) {
        currentSpeed += speedIncrease * 2
    }
    
    
    func brake(){
        
    }
}

class SportsCar: Vehicle {
    override init() {
        super.init()
        make = "BWM"
        model = "3 Series"
        print("I am the child")
    }
    
    override func drive(speedIncrease: Double) {
        currentSpeed += speedIncrease * 3
    }
}


