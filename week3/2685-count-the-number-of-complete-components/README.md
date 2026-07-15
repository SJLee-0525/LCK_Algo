# 2685. Count the Number of Complete Components (Medium)

- **링크**: https://leetcode.com/problems/count-the-number-of-complete-components/description/
- **주제**: Union-Find / Graph

## 문제 요약

무향 그래프에서 완전 연결 성분의 개수를 구한다. 완전 연결 성분은 모든 정점 쌍 사이에 간선이 존재하는 연결 성분을 의미한다.

### 예시

```
입력: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
출력: 3
설명: 모든 성분이 완전하다 (0-1-2, 3-4, 5)

입력: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
출력: 1
설명: 0-1-2는 완전하지만, 3-4-5는 4-5 간선이 없어 불완전하다.
```

### 제약

- 1 <= n <= 50
- 0 <= edges.length <= n * (n - 1) / 2

### 포인트

- 먼저 각 성분을 찾고(Union-Find 또는 DFS), 성분 크기 k에 대해 필요한 간선 개수는 k*(k-1)/2 (완전 그래프)이다.
- 각 성분이 이 개수를 만족하는지 확인해 완전성을 판단한다.

## 풀이

| 멤버   | 파일         | 시간 | 공간 |
| ------ | ------------ | ---- | ---- |
| Lucian | `lucian.py`  |      |      |
| Kevin  | `kevin.py`   |      |      |
| Chloe  | `chloe.java` |      |      |
