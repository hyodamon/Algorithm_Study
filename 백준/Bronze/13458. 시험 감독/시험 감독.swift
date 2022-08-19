import Foundation

let N = Int(readLine()!)!
var A: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }

let input: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
let B = input[0], C = input[1]

var cnt = 0

for a in A {
    var tmp = a
    tmp -= B
    cnt += 1
    if tmp > 0 {
        cnt += Int(ceil(Double(tmp) / Double(C)))
    }
    
}

print(cnt)