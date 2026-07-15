# 2492. Minimum Score of a Path Between Two Cities (Medium)

- **링크**: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
- **주제**: Union-Find / DFS

## 문제 요약

n개 도시와 양방향 도로 리스트가 주어진다. 도시 1에서 n까지 가는 경로의 점수는 경로 상 도로 거리의 최솟값이다. 경로 중 가능한 최대 점수를 반환한다 (같은 도로를 여러 번 사용할 수 있음).

### 예시

```
입력: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
출력: 5
설명: 1 -> 2 -> 4 경로의 점수는 min(9,5) = 5

입력: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
출력: 2
설명: 1 -> 2 -> 1 -> 3 -> 4의 점수는 min(2,2,4,7) = 2
```

### 제약

- 2 <= n <= 10^5
- 1 <= roads.length <= 10^5
- 1 <= distancei <= 10^4
- 1과 n 사이에는 항상 경로가 존재한다.

### 포인트

- 1과 n이 연결된 모든 도로에 접근할 수 있다면, 최대 점수는 결국 1과 n이 속한 연결 성분 내 최소 거리가 된다.
- Union-Find로 1과 n이 같은 성분에 속하는지 확인하면서 거리의 최솟값을 추적한다.

## 풀이

| 멤버   | 파일         | 시간 | 공간 |
| ------ | ------------ | ---- | ---- |
| Lucian | `lucian.py`  |      |      |
| Kevin  | `kevin.py`   |      |      |
| Chloe  | `chloe.java` |      |      |
