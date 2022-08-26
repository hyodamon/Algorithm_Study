import Foundation

typealias initVariabe = (cogwheels: [[Int]], K: Int) // 초기 변수

/// 초기 변수 입력 함수
func Input() -> initVariabe {
    var cogwheels: [[Int]] = []
    for _ in 0...3 {
        cogwheels.append(readLine()!.map{ Int(String($0))! })
    }
    let K = Int(readLine()!)!
    
    return (cogwheels, K)
}

/// 재귀를 통해 회전을 관리하는 함수
/// idx : 현재 움직일 톱니바퀴, dir : 방향, state : 움직인 톱니바퀴인지 상태를 확인하는 배열 (true면 이미 움직인 톱니바퀴, false면 아직 안 움직인 톱니바퀴)
func Rotate(idx: Int, dir: Int, state: [Bool]) {
    var tmpState = state
    tmpState[idx] = true
    
    if idx < 3 && cogwheels[idx][2] != cogwheels[idx + 1][6] && !state[idx + 1] {
        // 마지막 톱니바퀴가 아니고(idx가 3보다 작은), 맞물리는 곳의 극이 다르고, 그 톱니바퀴가 움직인 톱니바퀴가 아니면
        Rotate(idx: idx + 1, dir: -dir, state: tmpState) // 반대 방향(-dir)으로 Rotate
    }
    if idx > 0 && cogwheels[idx][6] != cogwheels[idx - 1][2] && !state[idx - 1] {
        // 첫 번째 톱니바퀴가 아니고(idx가 0보다 큰), 맞물리는 곳의 극이 다르고, 그 톱니바퀴가 움직인 톱니바퀴가 아니면
        Rotate(idx: idx - 1, dir: -dir, state: tmpState) // 반대 방향(-dir)으로 Rotate
    }
    
    // 방향에 맞게 돌려줌
    if dir == 1 {
        RotateRight(idx: idx)
    } else {
        RotateLeft(idx: idx)
    }
}


/// 시계 방향으로 회전하는 함수
func RotateRight(idx: Int) {
    let tmp = cogwheels[idx].last!
    cogwheels[idx].removeLast()
    cogwheels[idx].insert(tmp, at: 0)
}

/// 시계 반대 방향으로 회전하는 함수
func RotateLeft(idx: Int) {
    let tmp = cogwheels[idx].first!
    cogwheels[idx].removeFirst()
    cogwheels[idx].append(tmp)
}


/// 점수를 계산하는 함수
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

/// 명령어 입력
for _ in 0..<K {
    let command = readLine()!.split(separator: " ").map{ Int(String($0))! }
    Rotate(idx: command[0] - 1, dir: command[1], state: [false, false, false, false])
}

print(getScore())