# 3286. Find a Safe Walk Through a Grid (Medium)

- **링크**: https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
- **주제**: BFS / Graph Traversal

## 문제 요약

m x n 그리드와 health 값이 주어진다. (0,0)에서 시작해 (m-1, n-1)에 도달할 수 있는지 판단한다. grid[i][j] = 1인 셀은 health를 1 깎고, health가 양수여야 이동할 수 있다.

### 예시

```
입력: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1
출력: true

입력: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
출력: false
```

### 제약

- 1 <= m, n <= 50
- 2 <= m * n
- 1 <= health <= m + n
- grid[i][j] is 0 or 1

### 포인트

- BFS로 최단 경로를 찾되, 경로 상 위험 셀(1)의 개수를 추적해야 한다.
- 도착지에서 health가 1 이상 남아야 하므로, 최단 경로의 위험 셀 개수가 health보다 작아야 한다.

## 풀이

| 멤버   | 파일         | 시간 | 공간 |
| ------ | ------------ | ---- | ---- |
| Lucian | `lucian.py`  |      |      |
| Kevin  | `kevin.py`   |      |      |
| Chloe  | `chloe.java` |      |      |
