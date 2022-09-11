# [Silver II] 색종이 만들기 - 2630 

[문제 링크](https://www.acmicpc.net/problem/2630) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

분할 정복(divide_and_conquer), 재귀(recursion)

### 문제 설명

<p>아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images/bwxBxc7ghGOedQfiT3p94KYj1y9aLR.png" style="height:221px; width:215px"></p>

<p>전체 종이의 크기가 N×N(N=2<sup>k</sup>, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.</p>

<p>전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.</p>

<p>위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를 처음 나눈 후의 상태를, <그림 4>는 두 번째 나눈 후의 상태를, <그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 7장의 파란색 색종이를 보여주고 있다.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images/VHJpKWQDv.png" style="height:488px; width:487px"></p>

<p>입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.</p>

### 출력 

 <p>첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.</p>


### 풀이과정

문제 내용과 그림을 보았을 때, 계속해서 반으로 나눠가기 때문에 분할 정복을 사용해야 겠다고 판단했다.

**처음에 내가 푼 코드**
```python
import sys

N = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue = 0
white = 0

def recursion(n, r, c) :
    global blue, white
    sum = 0
    
    for i in range(r, r + n) :
        for j in range(c, c + n) :
            sum += paper[i][j]
    if sum == n ** 2 :
        blue += 1
    elif sum == 0 :
        white += 1
    else :
        half = n // 2
        recursion(half, r, c)
        recursion(half, r + half, c)
        recursion(half, r, c + half)
        recursion(half, r + half, c + half)
    

recursion(N, 0, 0)

print(white)
print(blue)
```
`recursion()`이라는 함수에 종이의 크기(N)과 시작 좌표(r, c)를 입력받는다. 그리고 입력받은 크기(N * N) 만큼 탐색하면서 모든 값들을 더해준다.
  
이때 더한 값이 다 더한 값이 n의 제곱 (n ** 2)이면 탐색한 영역의 종이는 파란색 종이라는 뜻이다. 반대로 0이라면 흰색 종이라는 뜻이다.
  이 둘에 모두 해당되지 않는다면, 더 분할을 해야 하는 종이이다!
  
  분할하는 방법은 half라는 현재 변의 크기의 반(n // 2)의 크기로 시작하는 좌표 4곳을 재귀로 다시 호출하는 것이다. 이렇게 되면 가장 작은 크기의 종이(n == 1) 까지 모두 탐색할 수 있기 때문에 원하는 답을 도출할 수 있다.
  
  다 풀고나서 채점도 맞았지만 뭔가 비효율적인 코드를 짠 것 같아서, 다른 사람의 코드를 살펴보았다.
  
  **다른 분들의 코드**
  ```python
  import sys

N = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue = 0
white = 0

def recursion(n, r, c) :
    global blue, white
    sum = 0
    
    tmp = paper[r][c]
    for i in range(r, r + n) :
        for j in range(c, c + n) :
            if paper[i][j] != tmp :
                half = n // 2
                recursion(half, r, c)
                recursion(half, r + half, c)
                recursion(half, r, c + half)
                recursion(half, r + half, c + half)
                return
            
    if tmp == 1 :
        blue += 1
    else :
        white += 1
    

recursion(N, 0, 0)

print(white)
print(blue)
  ```
  
 내 코드와 다른 점은, 탐색할 영역을 모두 더하지 않고 종이의 확인한 부분이 이전과 다르다면(paper[i][j] != tmp) 재귀를 호출하는 것이다.
  이로 인해, 내 코드의 비효율적인 점을 해결할 수 있었다.
