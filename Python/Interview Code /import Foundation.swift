import Foundation
import XCTest

/**
  THE PROBLEM: Our awesome new prime number generator has some bugs in it. We need to find them.
  THE SOLUTION: Regression tests! There are several correctness conditions for our generator:
    - output should contain only prime numbers
    - output list should contain no elements greater than the input integer
    - output list should be ordered.
  If all these correctness conditions were covered by tests, we could find the bug for sure.
*/

// MARK: PRIME NUMBER GENERATOR

/// sieve implements a simple Sieve of Eratosthenes prime number generator. 
/// It is used to generate an ordered array of prime numbers smaller than or equal to n.
/// - Parameter n: Upper bound of prime numbers to generate.
/// - Returns: Ordered array of prime numbers <= n
func sieve(_ n: Int) -> [Int] {
    print("Sieve is generating primes <= \(n)")
    guard n>=2 else { return [] }
    var primes: [Int?] = Array(0..<n)
    primes[0] = nil
    primes[1] = nil
    for coefficient in 2...n {
        for index in stride(from: coefficient, to: n, by: coefficient) {
            print("\(index) is divisible by \(coefficient), removing as non-prime.")
            primes[index] = nil
        }
    }
    return primes.reversed().compactMap { $0 }
}

// MARK: TEST CASES

class SieveTests: XCTestCase {
  static var allTests = {
    return [("testNoPrimesLessThan2", testNoPrimesLessThan2),
           ("testCase2", testCase2),
           ("testCase3", testCase3)]
  }()
  func testNoPrimesLessThan2() {
    XCTAssert(sieve(0).isEmpty, "No primes <= 0")
    XCTAssert(sieve(1).isEmpty, "No primes <= 1")
  }
  func testCase2() {
    // FILL IN TEST ASSERTIONS HERE TO FIND THE BUGS
    XCTAssert(true, "Test placeholder")
  }
  func testCase3() {
    // FILL IN TEST ASSERTIONS HERE TO FIND THE BUGS
    XCTAssert(true, "Test placeholder")
  }
}

XCTMain([testCase(SieveTests.allTests)])