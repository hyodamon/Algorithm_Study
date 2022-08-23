import Foundation

typealias initVariable = (N: Int, M: Int, r: Int, c: Int, d: Int)
let dr = [0, -1, 0, 1]
let dc = [-1, 0, 1, 0]
func input() -> initVariable {
    let NM = readLine()!.split(separator: " ").map { Int(String($0))! }
    let rcd = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    return initVariable(NM[0], NM[1], rcd[0], rcd[1], rcd[2])
}

func dfs(nr: Int, nc: Int, nd: Int, cnt: Int, chance: Int) -> Int {
    if chance == 4 {
        if board[nr + dr[(nd + 3) % 4]][nc + dc[(nd + 3) % 4]] == 1 {
            return cnt
        } else {
            return dfs(nr: nr + dr[(nd + 3) % 4], nc: nc + dc[(nd + 3) % 4], nd: nd, cnt: cnt, chance: 0)
        }
    }
    
    if board[nr][nc] == 0 {
        board[nr][nc] = 2
    }
    
    if board[nr + dr[nd]][nc + dc[nd]] == 0 {
        return dfs(nr: nr + dr[nd], nc: nc + dc[nd], nd: (nd + 3) % 4, cnt: cnt + 1, chance: 0)
    } else {
        return dfs(nr: nr, nc: nc, nd: (nd + 3) % 4, cnt: cnt, chance: chance + 1)
    }
}

let (N, M, r, c, d) = input()

var board: [[Int]] = []
for _ in 0..<N {
    board.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}


print(dfs(nr: r, nc: c, nd: d, cnt: 1, chance: 0))