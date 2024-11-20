import UIKit

class Vehicle {
    var tires = 4
    var make : String?
    var model : String?
    var currentSpeed: Double = 0
    
    init(){
        print("I Am the Parent")
    }
    
    func drive(speedIncrease: Double) -> Double {
        currentSpeed += speedIncrease * 2
        return currentSpeed
    
    }
    
    
    func brake(){
        print("brake")
    }
    

}

class SportsCar: Vehicle {
    override init() {
        super.init()
        make = "BWM"
        model = "3 Series"
        print("I am the child")
    }
    
    override func drive(speedIncrease: Double) -> Double {
        currentSpeed = speedIncrease * 100000
        return currentSpeed
        
    }
    
}

let car = SportsCar()
print(car.drive(speedIncrease: 100000))


