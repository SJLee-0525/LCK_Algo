# 125. Valid Palindrome (Easy)

- **링크**: https://leetcode.com/problems/valid-palindrome/
- **주제**: String / Two Pointers

## 문제 요약

문자열 `s`에 대해, 대문자를 소문자로 바꾸고 **영숫자(letters & numbers)가 아닌 문자를 모두 제거**한 뒤, 앞뒤로 읽었을 때 같으면 회문(palindrome)입니다. 회문이면 `true`, 아니면 `false`를 반환하세요.

### 예시

```
"A man, a plan, a canal: Panama" → true  ("amanaplanacanalpanama")
"race a car"                     → false
" "                              → true   (정제 후 빈 문자열)
```

### 제약

- `1 <= s.length <= 2 * 10^5`
- `s`는 출력 가능한 ASCII 문자로만 구성

### 포인트

- 투 포인터(좌/우)로 영숫자가 아닌 문자는 건너뛰며 비교 → O(n) 시간, O(1) 추가 공간.

## 풀이

| 멤버   | 파일                           | 시간 | 공간 |
| ------ | ------------------------------ | ---- | ---- |
| Lucian | `lucian.py` (또는 `lucian.js`) |      |      |
| Kevin  | `kevin.py`                     |      |      |
| Chloe  | `chloe.java`                   |      |      |
