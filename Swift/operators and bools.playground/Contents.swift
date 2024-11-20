import UIKit

var amIThebestTeacherEver :Bool = true
amIThebestTeacherEver = false

print(amIThebestTeacherEver)

if true == false || true == true {
    print("wtf")
}

var hasdatafinisheddownloading: Bool = false
//...
//...
hasdatafinisheddownloading = false

print(hasdatafinisheddownloading)

var bankbalance = 400
var itemtobuy = 400

if bankbalance >= itemtobuy {
    print("nice")
}

if itemtobuy == bankbalance {
    print("no")
}

var bookTitle1 = "Harry Potter and the Moppet of Mire"
var bookTitle2 = "Harry Potter and the Moppet of Mire"
 
if bookTitle1 != bookTitle2 {
    print("fix it")
}else if bookTitle2.count > 10{
    print("Books look great")
}




if !hasdatafinisheddownloading {
    print("Loading Data...")
}
