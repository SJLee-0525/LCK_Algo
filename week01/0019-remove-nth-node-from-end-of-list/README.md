# 19. Remove Nth Node From End of List (Medium)

- **링크**: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- **주제**: Linked List / Two Pointers

## 문제 요약

연결 리스트의 `head`가 주어질 때, **끝에서 n번째** 노드를 제거하고 변경된 리스트의 head를 반환하세요.

### 예시

```
head = [1,2,3,4,5], n = 2 → [1,2,3,5]
head = [1], n = 1         → []
head = [1,2], n = 1       → [1]
```

### 제약

- 노드 수 `sz`: `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`
- **Follow up**: 한 번의 순회(one pass)로 가능할까?

### 포인트

- 투 포인터: 앞 포인터를 n칸 먼저 보낸 뒤 둘이 함께 이동 → 앞이 끝에 닿으면 뒤가 삭제 대상 직전.
- head가 지워질 수 있으니 더미 노드를 쓰면 깔끔.

## 풀이

| 멤버   | 파일                           | 시간 | 공간 |
| ------ | ------------------------------ | ---- | ---- |
| Lucian | `lucian.py` (또는 `lucian.js`) |      |      |
| Kevin  | `kevin.py`                     |      |      |
| Chloe  | `chloe.java`                   |      |      |
