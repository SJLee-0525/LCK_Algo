# 122. Best Time to Buy and Sell Stock II (Medium)

- **링크**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
- **주제**: Array / Greedy / DP

## 문제 요약

정수 배열 `prices`(i일째 주가 `prices[i]`)가 주어집니다. 매일 사거나 팔 수 있지만, **동시에 최대 1주만 보유**할 수 있습니다. (같은 날 팔고 다시 사는 것은 허용) 얻을 수 있는 **최대 이익**을 반환하세요.

### 예시

```
prices = [7,1,5,3,6,4] → 7   (1에 사서 5에 팔고(+4), 3에 사서 6에 팔기(+3))
prices = [1,2,3,4,5]   → 4
prices = [7,6,4,3,1]   → 0   (이익 불가)
```

### 제약

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

### 포인트

- 그리디: 오르는 구간의 차이를 전부 더하면 됨. `prices[i] > prices[i-1]` 이면 `profit += prices[i] - prices[i-1]`.

## 풀이

| 멤버   | 파일                           | 시간 | 공간 |
| ------ | ------------------------------ | ---- | ---- |
| Lucian | `lucian.py` (또는 `lucian.js`) |      |      |
| Kevin  | `kevin.py`                     |      |      |
| Chloe  | `chloe.java`                   |      |      |
