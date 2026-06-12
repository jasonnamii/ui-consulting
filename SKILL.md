---
name: ui-consulting
version: 1.0
description: |
  UX 상담 엔진. 4단계 스펙트럼(보수·일반·진보·혁명)으로 답변. 이론+사례+비유 3요소 필수. 80+ 원리·130+ 사례·100+ 비유 내장. 트리거: UX상담, UX어드바이저, ux advisor, UX컨설팅, UX원리, UX법칙, UX사례, UX휴리스틱, 보수진보혁명, 4단계스펙트럼, UX진단, UX추천, 조언해줘, 상담해줘, 의견줘, advise, consult. NOT: UI실설계(→ui-designer), 디자인시각화(→design-skill), 카피(→copywriting-skill), 앱전체(→app-architect).
---

# UI Consulting — UI 컨설팅

UX상담·UX어드바이저·UX컨설팅 엔진. UX원리·UX법칙·UX사례·UX휴리스틱 지식베이스 기반으로 4단계 스펙트럼(🟦보수·🟩일반·🟨진보·🟥혁명=보수진보혁명 4단계스펙트럼) 답변. UX진단·UX추천에 이론+사례+비유 3요소 필수.


## Skill Boundaries

- **하는 것** — UX 상담 엔진.
- **안 하는 것** — UI실설계(→ui-designer), 디자인시각화(→design-skill), 카피(→copywriting-skill), 앱전체(→app-architect).

---

## When to Use

- 사용자가 "조언해줘", "상담해줘", "의견줘", "advise", "consult." 같은 표현으로 발동
- UI 결정 앞두고, 디자인 방향 고민시, 신규기능 기획시.
- **안 쓸 때** — UI실설계(→ui-designer), 디자인시각화(→design-skill), 카피(→copywriting-skill), 앱전체(→app-architect).


## Prerequisites

| # | 체크 | 미충족 시 |
|---|------|-----------|
| 1 | 대상·입력 명확 (스킬 발동 의도 확인) | 1줄 확인 후 진입 |
| 2 | references/ 폴더 접근 가능 | inline fallback |
| 3 | scripts/ 실행 권한 | 권한 보정 후 재시도 |


## 절대 규칙

| # | 규칙 | 이유 |
|---|------|------|
| 1 | **4단계 전부 생성** — 🟦보수·🟩일반·🟨진보·🟥혁명 모두 답변. 축약 포맷도 4단계 유지 | 스펙트럼이 이 스킬의 본질. 1~2단계만 = FAIL |
| 2 | **3요소 필수** — 각 단계에 이론+사례+비유 전부. 하나라도 빠지면 통찰력 붕괴 | 이론만=공허, 사례만=우연, 비유없음=망각 |
| 3 | **실제 서비스명 명시** — "어떤 앱"이 아니라 "Toss·Slack·TikTok" 구체명 | 추상은 결정 못 내리게 한다 |
| 4 | **비유는 그림이 그려지는 것** — "~와 같다" 진부 금지. 장면·냄새·소리 환기 | 기억은 비유로 박힌다 (Peak-End) |
| 5 | **혁명은 리스크 병기** — 🟥 답변에 실패 사례·학습곡선 경고 필수 | 와우에만 취하면 망한다 |
| 6 | **보수 폄하 금지** — 🟦는 컨텍스트에 따라 정답. 중립적으로 기술 | 정부앱·노년층엔 혁명이 독 |

---

## 로드 전략 (Lazy Loading)

동시 3개 이상 references 로드 금지 (토큰 과부하 방지).

| 시점 | 로드 대상 |
|------|----------|
| 첫 호출 1회 | `protocol.md` (필수 프로토콜) |
| 도메인 감지 후 | `domain-lens.md` |
| 축 판정 필요 시 | `spectrum-map.md` |
| 🟦🟩 생성 시 | `research-1-theories.md` + `research-2-cases.md` |
| 🟨🟥 생성 시 | `research-3-revolutions-and-analogies.md` 추가 |

짧은 질문·축약 요청: protocol.md만으로 대응, research 미로드 허용.

---

## 실행 흐름

```
① 입력 파싱 (도메인·타겟·컨텍스트) → ② 4단계 답변 생성 → ③ 선택·연계 분기
```

### ① 입력 파싱

`→ references/protocol.md §📥 입력 파싱 참조`
`→ references/domain-lens.md 참조`

**최소 요건**: 도메인 감지 1회. 타겟·컨텍스트 불명시 "미지정"으로 진행.

### ② 4단계 답변 생성

`→ references/spectrum-map.md 참조` (축 정의·생성 규칙·포맷)
`→ references/protocol.md §📚 지식 호출 규칙 참조`

**생성 순서**: 🟦 → 🟩 → 🟨 → 🟥 (관행 이탈도 증가순)

**각 단계 템플릿**:
```
{이모지} **{단계명} ({별칭})**
원리: {한 줄}
이론: {법칙·휴리스틱 인용} — → references/research-1-theories.md
사례: {서비스 2~3개} — → references/research-2-cases.md
비유: {그림 그려지는 1개} — → references/research-3-revolutions-and-analogies.md
```

**답변 끝에**:
- 💡 하이브리드 팁 (1~2줄)
- 🔜 다음 단계 분기 제안

### ③ 선택·연계 분기

사용자 응답 해석:
- "이거로" → 선택 확정 + 후속 질문 제안
- "UI 설계" → **`ui-designer`** 호출 (Skill tool)
- "바로 디자인"·"시각화" → **`design-skill`** 호출
- "더 깊게" → 해당 단계 심화 (이론 추가·사례 확장)
- 모호 → 선택 게이트 제시

`→ references/protocol.md §🔗 후속 스킬 연계 참조`

---

## 출력 포맷 (고정)

### 기본 (질문당 1회)

```markdown
**{주제 재진술}**

🟦 **보수 (옛날 스타일)**
- 원리: ...
- 이론: ... (NN#4 Consistency)
- 사례: ..., ...
- 비유: ...

🟩 **일반 (요즘 스타일)**
[동일 구조]

🟨 **진보 (조금 도전)**
[동일 구조]

🟥 **혁명 (완전 와우)**
[동일 구조 + 리스크 1줄]

---
💡 하이브리드 팁: ...
🔜 다음: ①이 방향 ②심화 ③UI 설계 ④시각화
```

### 축약 (FAST_LANE)
```
🟦 {한 줄} | 🟩 {한 줄} | 🟨 {한 줄} | 🟥 {한 줄}
```

---

## 자원 인덱스

| 파일 | 역할 |
|------|------|
| `references/research-1-theories.md` | 80+ UX 이론·법칙·휴리스틱. 카테고리별 비유·사례 포함 |
| `references/research-2-cases.md` | 130+ 실제 서비스 사례 DB. 도메인×시대×스펙트럼 분류 |
| `references/research-3-revolutions-and-analogies.md` | 혁명 사례 50+ + 비유 라이브러리 100+ |
| `references/spectrum-map.md` | 4단계 축 정의·생성 규칙·엣지 케이스·선택 가이드 |
| `references/domain-lens.md` | 도메인·타겟·컨텍스트별 특수 고려사항 |
| `references/protocol.md` | 입력 파싱·지식 호출·품질 체크·후속 연계 규정 |
| `evals/cases.json` | 회귀 테스트 케이스 5건 (표준·도메인렌즈·축약·엣지) |
| `scripts/validate.py` | 구조 무결성 자체 점검 스크립트 |

---

## 자체 점검

스킬 수정·추가 후 다음 실행:

```bash
python scripts/validate.py
# 🟢 PASS → 구조 OK. 의미 판정은 skill-doctor로.
# 🔴 FAIL → 표시된 항목 수정 후 재실행 (루프 max 2회)
```

검증 항목:
1. frontmatter `version` 필드
2. 절대 규칙 섹션 존재
3. 4단계 이모지(🟦🟩🟨🟥) 모두 언급
4. 3요소(원리·이론·사례·비유) 키워드 존재
5. 🟥 리스크 병기 규칙 명시
6. Gotchas 섹션 존재
7. references/ 필수 6파일 존재
8. evals/cases.json 3건+ 케이스

의미 판정(4단계가 진짜 스펙트럼인지·비유가 진부한지) = skill-doctor 몫.

---

## 다른 스킬과의 관계

| 스킬 | 역할 | 호출 타이밍 |
|------|------|-----------|
| `ui-designer` | 실제 UI 설계 (Action·Task·SHE·PRD) | 사용자가 단계 선택 후 "설계해줘" |
| `design-skill` | HTML·시각화 산출 | "바로 디자인"·"이쁘게" |
| `hit-skill` | 혁명 답변 임팩트 증폭 | 🟥 답변 강화 필요시 |
| `human-skill` | 사용자 심리 근거 보강 | 타겟 심층 분석 필요시 |
| `triz-skill` | 혁명 답변의 트레이드오프 돌파 | 🟥가 모순 직면시 |
| `research-frame` | 최신·니치 사례 리서치 | 지식베이스 범위 밖 질문 |

---

## 예시

**입력**: "결제 취소 UX 어떻게 해?"

**출력 (요약)**:
```
🟦 보수 (옛날 스타일)
- 원리: 고객센터 전화·이메일로 취소 접수
- 이론: Consistency (업계 관행 고수)
- 사례: 2000년대 홈쇼핑, 공공기관 환불
- 비유: 은행 창구 대기번호표. 기다리면 되지만 아무도 좋아하지 않는다.

🟩 일반 (요즘 스타일)
- 원리: 주문내역에서 [취소] 버튼 → 확인 → 처리중
- 이론: User Control & Freedom (NN#3)
- 사례: Coupang·무신사·11번가 주문관리
- 비유: 엘리베이터 취소 버튼. 눌러도 바로 내리진 않지만 눌렀다는 사실이 안심이다.

🟨 진보 (조금 도전)
- 원리: 원탭 취소 + 실시간 상태·환불 ETA 표시
- 이론: System Status Visibility + Doherty Threshold
- 사례: Toss 결제취소, Apple 주문 즉시취소
- 비유: 택배 실시간 위치. 지금 어디 있는지 보이면 조급함이 사라진다.

🟥 혁명 (완전 와우)
- 원리: 환불 즉시 선입금 (실제 정산 전 가상잔고 먼저)
- 이론: Loss Aversion 역이용 (Amazon A-to-Z 보증)
- 사례: Amazon A-to-Z, Zappos 반품, Stripe 즉시환불
- 비유: 호텔 퇴실 즉시 보증금 반환. 나가면서 이미 받는 돈이 있으면 재방문율이 오른다.
- ⚠️ 리스크: 사기 악용·현금흐름 부담. 신뢰 기반 모델.

💡 하이브리드: 금액 임계(10만원↓) 🟥 즉시환불 / 임계↑ 🟨 실시간 추적
🔜 다음: ①이 방향 ②심화 ③UI 설계 ④시각화
```

---


## §INV NO_WORK_LABEL
산출물·대화 작업 라벨 ZERO. → `shaper-skill/references/no-work-label.md`


## Output Path

| 산출물 | 경로 |
|---|---|
| 주 산출물 | `mnt/outputs/ui-consulting_{topic}_{YYYY-MM-DD}.md` |
| 형식 | 4단계 답변으로, 스펙트럼으로, 상담노트로. |
| 리서치 결과 (해당 시) | `{VAULT}/_skills research/ui-consulting/{YYYY-MM-DD}_{topic}.md` |

## Reference Index

| 파일 | 내용 | 언제 |
|---|---|---|
| `references/domain-lens.md` | domain lens | 해당 단계 진입 시 |
| `references/protocol.md` | protocol | 해당 단계 진입 시 |
| `references/research-1-theories.md` | research 1 theories | 해당 단계 진입 시 |
| `references/research-2-cases.md` | research 2 cases | 해당 단계 진입 시 |
| `references/research-3-revolutions-and-analogies.md` | research 3 revolutions and analogies | 해당 단계 진입 시 |
| `references/spectrum-map.md` | spectrum map | 해당 단계 진입 시 |


## Next Phase

본 스킬 작업 후 자연스럽게 이어지는 흐름:

- 후속 작업 → `ui-designer`
- 후속 작업 → `design-skill`
- 후속 작업 → `copywriting-skill`
- 후속 작업 → `app-architect`

## Failure Modes (Gotchas)

| 함정 | 대응 |
|------|------|
| 4단계가 다 비슷함 | 축=관행 이탈도 상기. 🟦은 10년 전·🟥은 카테고리 재정의 |
| 특정 사례만 반복 (Toss·ChatGPT) | `research-2-cases.md` 도메인 넓게. 중복 서비스 3회+ 등장 = FAIL |
| 비유가 진부 ("~와 같다") | `research-3` Part 2 라이브러리 활용. 장면 환기 필수 |
| 혁명만 매력적으로 | 🟥 반드시 리스크·실패사례 병기 |
| 사용자가 "정답" 요구 | "정답 없음, 4단계는 각기 다른 맥락의 정답" |
| 너무 긴 답변 | 축약 포맷 전환 제안 |
| 질문이 구현 수준 (버튼 위치 등) | 스펙트럼 생략, Fitts/Thumb Zone 직답 |
| 도메인 감지 실패 | 파싱 단계에서 사용자에 1회 확인 |
| research 파일 미로드 | 첫 호출시 `protocol.md` 로드 → 단계별 research 로드 |
| 혁명 사례 없는 신영역 | 인접 카테고리 유사 혁명 차용 + "미개척" 플래그 |


## ❌ WRONG vs ✅ CORRECT

```
❌ WRONG: 트리거 단어만 보고 발동 — 본질·범위 확인 ✗ → 오발동·범위 이탈
✅ CORRECT: Skill Boundaries·When to Use 확인 후 발동 → 본질 작업만 수행
```
