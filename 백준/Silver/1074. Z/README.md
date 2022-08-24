# [Silver I] Z - 1074 

[문제 링크](https://www.acmicpc.net/problem/1074) 

### 성능 요약

메모리: 79512 KB, 시간: 12 ms

### 분류

분할 정복(divide_and_conquer), 재귀(recursion)

### 문제 설명

<p>한수는 크기가 2<sup>N</sup> × 2<sup>N</sup>인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/21c73b56-5a91-43aa-b71f-9b74925c0adc/-/preview/" style="width: 100px; height: 99px;"></p>

<p>N > 1인 경우, 배열을 크기가 2<sup>N-1</sup> × 2<sup>N-1</sup>로 4등분 한 후에 재귀적으로 순서대로 방문한다.</p>

<p>다음 예는 2<sup>2</sup> × 2<sup>2</sup> 크기의 배열을 방문한 순서이다.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/adc7cfae-e84d-4d5c-af8e-ee011f8fff8f/-/preview/" style="width: 250px; height: 252px;"></p>

<p>N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.</p>

<p>다음은 N=3일 때의 예이다.</p>

<p style="text-align:center"><img alt="" src="https://upload.acmicpc.net/d3e84bb7-9424-4764-ad3a-811e7fcbd53f/-/preview/" style="width: 533px; height: 535px;"></p>

### 입력 

 <p>첫째 줄에 정수 N, r, c가 주어진다.</p>

### 출력 

 <p>r행 c열을 몇 번째로 방문했는지 출력한다.</p>

### 풀이과정

문제 설명에서 재귀라는 힌트를 주어서 재귀를 사용해서 풀어야 한다는 것을 파악했다. 하지만 분할 정복이라는 것을 생각하지 못 해 문제를 푸는 시간이 정말 오래걸렸다.

1. 문제의 모든 규칙은 Z에 모양대로 1, 2, 3, 4 순서로 움직이기 때문에 이와 맞게 4등분으로 분할해야한다. 그래서 먼저 가로, 세로의 절반 길이 값을(half) 구해준다. -> 2<sup>N</sup>의 반

2. 그리고 분할된 사분면 마다 첫 번째 값는 half의 제곱의 배수이다.

![](https://velog.velcdn.com/images/hyoda_mon/post/cf72d00f-f42f-445e-8fed-2bafd450b374/image.png)

위와 같이 N이 3일 때, half는 4(2<sup>3</sup> / 2) 이고 각 사분면의 첫 번째 값은 4<sup>2</sup>의 배수이다. (16, 32, 48)

3. 그래서 가로, 세로마다 위에서 구한 half를 넘는지 아닌지 판별하여 N은 1씩, 가로, 세로 길이는 half 만큼 줄여가며, 결과 값(result)에는 사분면의 첫 번째 값을 더해준다.

4. N이 1이 되었을 때, 가장 작은 Z 형태 (0, 1, 2, 3)에 이제까지 더한 결과 값(result)를 더하면 된다.


![](https://velog.velcdn.com/images/hyoda_mon/post/7bf8b0f2-4da3-4b34-aea1-8837ca307aa7/image.png)

예를 들어 N이 3일 때 r = 6, c = 3 인 값을 찾으려 한다 해보자.
half는 4(2<sup>3</sup> / 2)이고 (6, 3)은 3사분면에 있기 때문에 3사분면에 첫 번째 값인 32를 더해준다.
그리고 분할된 사분면(N = 2)에서 또 4분면에 속하기 때문에 12를 더해준다.
N = 1이 되었으므로 Z 형태의 2번 째 값인 1을 더해준다.
그럼 **32 + 12 + 1 = 45** 라는 정답을 금방 구할 수 있다!
