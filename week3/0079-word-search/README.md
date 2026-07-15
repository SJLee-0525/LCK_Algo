# 79. Word Search (Medium)

- **링크**: https://leetcode.com/problems/word-search/
- **주제**: Backtracking / DFS

## 문제 요약

m x n 문자 그리드와 문자열 word가 주어진다. word가 그리드에 존재하는지 판단한다. 인접한 셀(상하좌우)에서 순차적으로 문자를 찾아야 하며, 같은 셀을 여러 번 사용할 수 없다.

### 예시

```
입력: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
출력: true

입력: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
출력: true

입력: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
출력: false
```

### 제약

- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word는 대소문자 영문자로만 이루어짐

### 포인트

- 각 셀에서 시작하는 DFS/백트래킹으로 word를 찾는다.
- 방문한 셀을 표시해 같은 셀을 재사용하지 않도록 주의한다. (복원도 필요)
- Early termination으로 word를 모두 매칭하면 즉시 true를 반환할 수 있다.

## 풀이

| 멤버   | 파일         | 시간 | 공간 |
| ------ | ------------ | ---- | ---- |
| Lucian | `lucian.py`  |      |      |
| Kevin  | `kevin.py`   |      |      |
| Chloe  | `chloe.java` |      |      |
