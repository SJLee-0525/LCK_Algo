# 참여 가이드

규칙은 최소한만. 문제 푸는 것보다 여기에 힘이 더 들면 안 됩니다.

## 핵심 3가지

1. `main`에 직접 푸시하지 말고 PR로 올린다
2. 브랜치는 주차 단위 하나: `이름/week01`
3. 본인 파일만 건드린다 (남의 풀이는 PR 코멘트로)

## 흐름

한 주에 브랜치 하나 파고, 그 주 문제들을 거기 쌓은 뒤 마지막에 PR 한 번.

```bash
git checkout main && git pull
git checkout -b kevin/week01

# 문제 풀 때마다 커밋 (메시지는 자유)
git add week01/0155-min-stack/kevin.py
git commit -m "Min Stack"
git push -u origin kevin/week01   # 이후엔 git push

# 그 주 풀이가 모이면 GitHub에서 PR 생성 (제목 예: [Kevin] week01)
```

## 파일 위치

`week{NN}/{문제번호 4자리}-{slug}/{이름}.{확장자}`

- 확장자: lucian `.py`/`.js`, kevin `.py`, chloe `.java`
- 파일 맨 위에 링크/접근/복잡도 한두 줄 메모면 충분

## 리뷰

서로 PR 코멘트로 풀이 보고 배우는 게 목적입니다. 승인 강제 게이트는 두지 않아요 — 코멘트 한 번씩 보고 본인이 머지하면 됩니다. 머지 후 작업 브랜치는 삭제.

진도표(`weekNN/README.md`, 루트 `README.md`)는 머지하면서 체크 갱신, 까먹으면 다음 PR에 같이.

## 포맷

문서(`.md`) 등을 고쳤으면 커밋 전에 `npm run format` 한 번. 처음엔 `npm install` 먼저. (Python·Java 코드는 각자 포매터 사용)

## 더 빡세게 하고 싶을 때 (선택)

main을 보호하고 싶으면 GitHub Settings → Branches → `main`에 "Require a pull request before merging"만 켜면 됩니다. 승인 필수까지는 스터디엔 과할 수 있어요.
