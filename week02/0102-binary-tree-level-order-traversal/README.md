# 102. Binary Tree Level Order Traversal (Medium)

- **링크**: https://leetcode.com/problems/binary-tree-level-order-traversal/
- **주제**: Tree / BFS

## 문제 요약

이진 트리의 루트가 주어질 때, 노드 값을 레벨 순서대로(위에서 아래로, 각 레벨은 왼쪽에서 오른쪽으로) 묶어서 반환하세요.

### 예시

```
root = [3,9,20,null,null,15,7]   → [[3],[9,20],[15,7]]
root = [1]                       → [[1]]
root = []                        → []
```

### 제약

- 노드 수는 `[0, 2000]` 범위
- `-1000 <= Node.val <= 1000`

### 포인트

- 힌트: 큐를 쓰는 너비 우선 탐색(BFS)이 자연스럽습니다. 각 반복에서 "현재 큐에 들어있는 개수"만큼만 처리하면 레벨 경계를 나눌 수 있습니다.

## 풀이

| 멤버   | 파일                           | 시간 | 공간 |
| ------ | ------------------------------ | ---- | ---- |
| Lucian | `lucian.py` (또는 `lucian.js`) |      |      |
| Kevin  | `kevin.py`                     |      |      |
| Chloe  | `chloe.java`                   |      |      |
