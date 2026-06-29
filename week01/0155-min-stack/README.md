# 155. Min Stack (Medium)

- **링크**: https://leetcode.com/problems/min-stack/
- **주제**: Stack / Design

## 문제 요약

push, pop, top, 그리고 **최솟값 조회(getMin)** 를 모두 **O(1)** 에 지원하는 스택을 설계하세요.

`MinStack` 클래스 구현:

- `MinStack()` — 객체 초기화
- `void push(int val)` — `val`을 스택에 push
- `void pop()` — top 원소 제거
- `int top()` — top 원소 반환
- `int getMin()` — 스택의 최솟값 반환

각 연산은 **O(1)** 시간이어야 합니다.

### 예시

```
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
→ [null,null,null,null,-3,null,0,-2]
```

### 제약

- `-2^31 <= val <= 2^31 - 1`
- `pop`, `top`, `getMin` 은 항상 비어있지 않은 스택에서 호출됨
- 최대 `3 * 10^4` 번 호출

### 포인트

- 힌트: 각 원소를 push할 때 "그 시점까지의 최솟값"을 함께 들고 있으면 됩니다. (보조 스택 또는 (값, 현재최솟값) 쌍)

## 풀이

| 멤버   | 파일                           | 시간 | 공간 |
| ------ | ------------------------------ | ---- | ---- |
| Lucian | `lucian.py` (또는 `lucian.js`) |      |      |
| Kevin  | `kevin.py`                     |      |      |
| Chloe  | `chloe.java`                   |      |      |
