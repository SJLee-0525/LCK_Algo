# 98. Validate Binary Search Tree (Medium)

- **링크**: https://leetcode.com/problems/validate-binary-search-tree/
- **주제**: Tree / DFS / BST

## 문제 요약

이진 트리의 `root`가 주어질 때, 유효한 **이진 탐색 트리(BST)** 인지 판별하세요.

유효한 BST 정의:

- 노드의 **왼쪽 서브트리**는 그 노드보다 **엄격히 작은** 값만 포함
- 노드의 **오른쪽 서브트리**는 그 노드보다 **엄격히 큰** 값만 포함
- 좌·우 서브트리도 각각 BST여야 함

### 예시

```
root = [2,1,3]                 → true
root = [5,1,4,null,null,3,6]   → false  (루트 5인데 오른쪽 자식이 4)
```

### 제약

- 노드 수: `[1, 10^4]`
- `-2^31 <= Node.val <= 2^31 - 1`

### 포인트

- 흔한 함정: 부모와만 비교하면 안 됨. 각 노드에 허용 범위 `(min, max)` 를 전달하며 검사.
- 또는 **중위순회(inorder)** 결과가 엄격히 증가하는지 확인.

## 풀이

| 멤버   | 파일                           | 시간 | 공간 |
| ------ | ------------------------------ | ---- | ---- |
| Lucian | `lucian.py` (또는 `lucian.js`) |      |      |
| Kevin  | `kevin.py`                     |      |      |
| Chloe  | `chloe.java`                   |      |      |
