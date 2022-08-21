import Foundation

let N = Int(readLine()!)!
let solutions = readLine()!.split(separator: " ").map{ Int(String($0))! }

var diff = 2_000_000_000
var result: (Int, Int) = (0, 0)

var first = 0, last = solutions.count - 1

while first != last {
    let curDiff = abs(solutions[first] + solutions[last])
//    print("curDiff : \(curDiff)")
//    print("first : \(solutions[first]), last : \(solutions[last])")
    if curDiff == 0 {
        result.0 = solutions[first]
        result.1 = solutions[last]
        break
    }
    
    if curDiff < diff {
        diff = curDiff
        result.0 = solutions[first]
        result.1 = solutions[last]
    }
    
    if solutions[first] + solutions[last] < 0 {
        first += 1
    } else {
        last -= 1
    }
}

print(result.0, result.1)