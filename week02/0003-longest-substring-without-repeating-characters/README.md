# 3. Longest Substring Without Repeating Characters (Medium)

- **링크**: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- **주제**: String / Sliding Window

## 문제 요약

문자열 `s`가 주어질 때, 중복 문자가 없는 가장 긴 부분 문자열(substring)의 길이를 구하세요. 부분 문자열은 연속해야 합니다(부분 수열 아님).

### 예시

```
s = "abcabcbb"   → 3   ("abc")
s = "bbbbb"      → 1   ("b")
s = "pwwkew"     → 3   ("wke")
```

### 제약

- `0 <= s.length <= 5 * 10^4`
- `s`는 영문자, 숫자, 기호, 공백으로 구성

### 포인트

- 힌트: 두 포인터로 윈도우를 유지하는 슬라이딩 윈도우. 문자의 마지막 등장 위치를 기록해 두면 중복이 생겼을 때 왼쪽 경계를 한 번에 당길 수 있습니다.

## 풀이

| 멤버   | 파일                           | 시간 | 공간 |
| ------ | ------------------------------ | ---- | ---- |
| Lucian | `lucian.py` (또는 `lucian.js`) |      |      |
| Kevin  | `kevin.py`                     |      |      |
| Chloe  | `chloe.java`                   |      |      |
