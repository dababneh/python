import UIKit

class Solution {
    func fib(_ N: Int) -> Int {
        if N < 2 {
            return N
        }
        var a = 0
        var b = 1
        for _ in 2...N {
            let temp = b
            b += a
            a = temp
        }
        return b
    }
}

var test = Solution()

test.fib(5)


