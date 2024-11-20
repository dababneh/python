import UIKit

let allowedEntry = false
if !allowedEntry {
    print("access denied")
}

let enteredDoorCode = true
let passedRetinaScan = false
let iAmTom = false

if enteredDoorCode && passedRetinaScan || iAmTom {
    print("Welcome")
} else {
    print("Access denied again")
}

let hasDoorKey = false
let KnowsOvverride = true

if hasDoorKey || KnowsOvverride {
    print("welcome ")
} else{
    print("No welcome baby")
}
