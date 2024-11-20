import UIKit
import Foundation

var palindromes: [String] = [
  // Valid
  "racecar",
  "Kayak",
  "never odd or even",
  "rats live on no evil star",
  "A Toyota! Race fast... safe car: a Toyota",
  "Some men interpret nine memos",
  // Invalid
  "wombat",
  "No lemons, one melon", // lemons, one->lemon, no
  "Too bad – I hid a book", // book->boot
  "No trace; not one cartoon", // cartoon->carton
  "Ma'am, I'm Adam", // Ma'am->Madam
  "Del was a sled", // was->saw
  "Flee to Em, remote elf", // Em->me
  "Ma? Ha! A sham!" // Ha! A sham->Has a ham
]

func isPalindrome(_ palindrome: String) -> Bool {
    for i in 1...palindrome.count {
        if palindrome[i] == palindrome[palindrome.c]
    }
}

print("- Check palindromes -\n")

print(isPalindrome("never odd or even"))

