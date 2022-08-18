let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = input[0], P = input[1], Q = input[2]

var dp: [Int:Int] = [0:1]

func dfs(_ i : Int) -> Int {
    if dp[i] != nil {
        return dp[i]!
    }
    dp[i] = dfs(i / P) + dfs(i / Q)
    return dp[i]!
}

print(dfs(N))