/*
 
 한 의상의 종류 내에 있는 의상의 수를 N라고 한다면, 그 의상의 종류를 선택할 수 있는 경우의 수는 N + 1이다.
 왜냐하면, 전체 중 한 가지(N)와 아무 옷도 선택하지 않을 경우의 수(1)을 합쳐서 이다.
 
 그래서 A, B, C라는 의상의 종류가 있고, 각 종류마다 가지고 있는 의상의 수를 a, b, c라고 한다면
 (a + 1) * (b + 1) * (c + 1) - 1 를 해줘야한다.
 -1를 하는 이유는 A, B, C 중 아무 것도 입지 않을 경우의 수를 빼주는 것 이다.
 
 */

import Foundation

func main() {
    let T = Int(readLine()!)! // 테스트 케이스 수
    
    for _ in 0..<T {
        let N = Int(readLine()!)! // 의상의 수
        var clothesDict: Dictionary<String, [String]> = [:] // 의상을 저장할 Dictionary
        for _ in 0..<N {
            let input = readLine()!.components(separatedBy: " ") // 입력받고 공백으로 자름
            
            if clothesDict[input.last!] == nil { // key값이 없다면, 생성
                clothesDict[input.last!] = [input.first!]
            } else { // 있다면, append
                clothesDict[input.last!]?.append(input.first!)
            }
        }
        
        var cnt = 1
        for clothes in clothesDict {
            cnt *= clothes.value.count + 1
        }
        print(cnt - 1)
    }
    
}

main()