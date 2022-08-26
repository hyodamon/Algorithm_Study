import Foundation
typealias initVariabe = (cogwheels: [[Int]], K: Int)

func Input() -> initVariabe { // 초기 변수 입력
    var cogwheels: [[Int]] = []
    for _ in 0...3 {
        cogwheels.append(readLine()!.map{ Int(String($0))! })
    }
    let K = Int(readLine()!)!
    
    return (cogwheels, K)
}

func Rotate(idx: Int, dir: Int, state: [Bool]) {
    var tmpState = state
    tmpState[idx] = true
    
    if idx < 3 && cogwheels[idx][2] != cogwheels[idx + 1][6] && !state[idx + 1] {
        Rotate(idx: idx + 1, dir: -dir, state: tmpState)
    }
    if idx > 0 && cogwheels[idx][6] != cogwheels[idx - 1][2] && !state[idx - 1] {
        Rotate(idx: idx - 1, dir: -dir, state: tmpState)
    }
    
    if dir == 1 {
        RotateRight(idx: idx)
    } else {
        RotateLeft(idx: idx)
    }
}

func RotateRight(idx: Int) {
    let tmp = cogwheels[idx].last!
    cogwheels[idx].removeLast()
    cogwheels[idx].insert(tmp, at: 0)
}

func RotateLeft(idx: Int) {
    let tmp = cogwheels[idx].first!
    cogwheels[idx].removeFirst()
    cogwheels[idx].append(tmp)
}

func getScore() -> Int {
    var score = 0
    for idx in 0...3 {
        if cogwheels[idx][0] == 1 { // 톱니바퀴의 12시 방향의 극
            score += Int(pow(2.0, Double(idx))) // 2의 제곱수 만큼 점수가 늘어나기 때문
        }
    }
    return score
}

var (cogwheels, K) = Input()

for _ in 0..<K {
    let command = readLine()!.split(separator: " ").map{ Int(String($0))! }
    Rotate(idx: command[0] - 1, dir: command[1], state: [false, false, false, false])
}

print(getScore())