//
//  main.swift
//  BOJ
//
//  Created by Yang Hyojun on 2022/08/30.
//

import Foundation

typealias inputVariable = (N: Int, L:Int, R:Int)
let (dr, dc) = ([-1, 1, 0, 0], [0, 0, 1, -1])

func Input() -> inputVariable {
    let NLR = readLine()!.split(separator: " ").map{ Int(String($0))! }
    let N = NLR[0], L = NLR[1], R = NLR[2]
    return (N, L, R)
}

func BFS(_ startR: Int, _ startC: Int) -> Int {
    visited[startR][startC] = 1
    var union = [(startR, startC)], queue = [(startR, startC)]
    var sum = A[startR][startC], cnt = 1

    while !queue.isEmpty {
        let (r, c) = queue.removeFirst()
        for i in 0..<4 {
            let nr = r + dr[i], nc = c + dc[i]

            if nr < 0 || nc < 0 || nr >= N || nc >= N { continue }

            if visited[nr][nc] == 1 { continue }

            if abs(A[r][c] - A[nr][nc]) >= L && abs(A[r][c] - A[nr][nc]) <= R  {
                visited[nr][nc] = 1
                union.append((nr, nc))
                cnt += 1
                sum += A[nr][nc]
                queue.append((nr, nc))
            }
        }
    }

    let avg = Int(floor(Double(sum) / Double(cnt)))
    for (r, c) in union {
        A[r][c] = avg
    }

    return cnt
}

let (N, L, R) = Input()
let blank = Array(repeating: Array(repeating: 0, count: N), count: N)
var visited = Array(repeating: Array(repeating: 0, count: N), count: N)
var A: [[Int]] = []
for _ in 0..<N {
    A.append(readLine()!.split(separator: " ").map{ Int(String($0))! })
}

var answer = 0

while true {
    var chk = false
    visited = Array(repeating: Array(repeating: 0, count: N), count: N)

    for r in 0..<N {
        for c in 0..<N {
            if (visited[r][c] == 0) {
                if BFS(r, c) >= 2 {
                    chk = true
                }
            }
        }
    }

    if !chk {
        break
    }

    answer += 1
}

print(answer)
