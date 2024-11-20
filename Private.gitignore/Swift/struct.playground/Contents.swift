import UIKit



class ScreenViewModel {
    let title:String
    var showButton:Bool
    
    init(title: String, showButton: Bool) {
        self.title = title
        self.showButton = showButton
        
        }
    func wow () -> String {
       return "wow"
    }
    
    
}

