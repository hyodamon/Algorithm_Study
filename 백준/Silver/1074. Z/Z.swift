import Foundation

let input = readLine()!.split(separator: " ").map{ Int(String($0))! }
let N = input[0], R = input[1], C = input[2]
let Z = [[0, 1], [2, 3]]

func recursion(n: Int, r: Int, c: Int, result: Double) -> Int {
    if n == 1 {
        return Z[r][c] + Int(result)
    }

    let half = Int(pow(2.0, Double(n)) / 2)
    
    if r < half && c < half  { // 1사분면
        return recursion(n: n - 1, r: r, c: c, result: result)
    } else if r < half && c >= half { // 2사분면
        return recursion(n: n - 1, r: r, c: c - half, result: result + pow(Double(half), 2.0))
    } else if r >= half && c < half { // 3사분면
        return recursion(n: n - 1, r: r - half, c: c, result: result + pow(Double(half), 2.0) * 2)
    } else { // 4사분면
        return recursion(n: n - 1, r: r - half, c: c - half, result: result + pow(Double(half), 2.0) * 3)
    }
}

print(recursion(n: N, r: R, c: C, result: 0))