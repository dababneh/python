import UIKit

var namesOfIntegers = [Int : String] ()
namesOfIntegers[3] = "Three"
namesOfIntegers[44] = "Forty Four"
namesOfIntegers = [:]

var airports : [String : String ] = ["yyz" : "TOronto", "LAX" :  "Los Angeles"]
print(" the bla bla bla has \(airports.count) itetms")
airports["LHR"] = "London"
airports["DEV"] = "London lalalala"
airports["DEV"] = nil

for (airportcode, airportname) in airports {
    print ("\(airportcode)")
}
print(airports)


