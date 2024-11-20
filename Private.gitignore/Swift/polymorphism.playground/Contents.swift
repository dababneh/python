import UIKit

class Shape {
   
    var area : Double?
    
    func calculateArea(valA: Double, valB: Double) {
    }
    init(area: Double? = nil) {
        self.area = area
    }
}

class Triangle: Shape {
   
    override func calculateArea(valA: Double, valB: Double) {
        return area = (valA * valB) / 2
    }
}

class Rectangle: Shape {
   
    override func calculateArea (valA: Double, valB: Double) {
        return area = (valA * valB)
    }
    
}







