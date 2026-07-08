# 88. Merge Sorted Array (Easy)

- **링크**: https://leetcode.com/problems/merge-sorted-array/
- **주제**: Array / Two Pointers

## 문제 요약

오름차순으로 정렬된 두 배열 `nums1`, `nums2`와 각각의 원소 개수 `m`, `n`이 주어집니다. 두 배열을 정렬 상태로 합쳐 `nums1`에 저장하세요. `nums1`의 길이는 `m + n`이고, 뒤쪽 `n`칸은 0으로 채워져 있어 무시합니다. 값을 반환하지 않고 `nums1`을 제자리에서 수정합니다.

### 예시

```
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3   → [1,2,2,3,5,6]
nums1 = [1], m = 1, nums2 = [], n = 0                   → [1]
nums1 = [0], m = 0, nums2 = [1], n = 1                   → [1]
```

### 제약

- `nums1.length == m + n`, `nums2.length == n`
- `0 <= m, n <= 200`, `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

### 포인트

- 힌트: 앞에서부터 채우면 기존 값을 덮어씁니다. 뒤(가장 큰 값)에서부터 채워 넣으면 덮어쓸 걱정 없이 O(m + n)에 끝낼 수 있습니다.

## 풀이

| 멤버   | 파일                           | 시간 | 공간 |
| ------ | ------------------------------ | ---- | ---- |
| Lucian | `lucian.py` (또는 `lucian.js`) |      |      |
| Kevin  | `kevin.py`                     |      |      |
| Chloe  | `chloe.java`                   |      |      |
