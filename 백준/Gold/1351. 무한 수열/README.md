# [Gold V] 무한 수열 - 1351 

[문제 링크](https://www.acmicpc.net/problem/1351) 

### 성능 요약

메모리: 69108 KB, 시간: 12 ms

### 분류

자료 구조(data_structures), 다이나믹 프로그래밍(dp), 해시를 사용한 집합과 맵(hash_set)

### 문제 설명

<p>무한 수열 A는 다음과 같다.</p>

<ul>
	<li>A<sub>0</sub> = 1</li>
	<li>A<sub>i</sub> = A<sub>⌊i/P⌋</sub> + A<sub>⌊i/Q⌋</sub> (i ≥ 1)</li>
</ul>

<p>N, P와 Q가 주어질 때, A<sub>N</sub>을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 3개의 정수 N, P, Q가 주어진다.</p>

### 출력 

 <p>첫째 줄에 A<sub>N</sub>을 출력한다.</p>

### 풀이 과정

Hash를 사용해서 푸는 문제라고 알고 풀긴 했지만, 문제를 보고 단순 DP문제라 생각했다. 그래서 Array를 이용해서 풀었더니 메모리 초과가 났다.

그래서 Hash를 사용해서 어떻게 풀 수 있을까 고민해보다, dictionary를 이용해 나올 수 있는 값들만 key와 value로 저장해준다면 같은 수열의 중복을 없애 메모리 초과를 내지 않을 수 있다.

