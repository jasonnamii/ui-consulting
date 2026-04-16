# ux-advisor

🇺🇸 [English README](./README.md)

**UX 질문 하나에 4단계(🟦보수·🟩일반·🟨진보·🟥혁명) 스펙트럼으로 답하는 상담 엔진. 이론·사례·비유 3요소 필수.**

## 사전 요건

- **Claude Cowork 또는 Claude Code** 환경

## 목적

UX 조언은 보통 "이게 베스트다" 단답이거나 "상황에 따라 다르다" 공허한 말로 끝난다. ux-advisor는 **한 질문에 네 개의 답**을 병렬로 낸다 — 10년 전 관행부터 카테고리 자체를 뒤집는 혁명까지. 각 답은 **원리 + 실제 서비스명 + 그림이 그려지는 비유** 세 요소를 반드시 갖춰서, 추상적 조언이 아니라 결정 가능한 선택지가 된다.

## 언제·어떻게 쓰나

UX 결정을 앞두고 쓴다. 온보딩·결제·내비·알림·피드·에러 처리 등 "이걸 어떻게 짜지?"라는 질문 전부. 자연어로 물으면("결제 취소 UX 어떻게?") 4단계 스펙트럼이 나오고, 방향을 골라서 **ui-action-designer**(실제 UI 설계) 또는 **design-skill**(바로 시각화)로 넘기면 된다.

## 사용 시나리오

| 상황 | 프롬프트 | 동작 |
|---|---|---|
| 디자인 결정 대기 | `"결제 취소 UX 어떻게 해?"` | Toss/Amazon/Stripe 사례 + 비유 포함 4단계 답 |
| 경쟁사 분석 후 방향잡기 | `"온보딩 어떻게 짜지?"` | 보수→혁명 스펙트럼 (Windows→Slack→Duolingo→ChatGPT) |
| 차별화 전략 수립 | `"피드 구조 추천해줘"` | 시간순→알고리즘→하이브리드→FYP식 리스크 프로파일 매핑 |
| 기능 아이디에이션 | `"알림 설계 조언"` | 즉시푸시→DND→Slack 멘션→BeReal 하루1번 |

## 핵심 기능

- **4단계 스펙트럼**: 🟦 보수(10년+ 관행) · 🟩 일반(현재 주류) · 🟨 진보(주류+변주) · 🟥 혁명(카테고리 재정의)
- **3요소 포맷**: 모든 답변에 이론+실제 서비스명+기억에 박히는 비유 — 추상 금지
- **80+ UX 원리 내장**: Nielsen 휴리스틱, 게슈탈트, Fitts/Hick/Miller/Tesler, 행동경제학, 접근성
- **130+ 사례 DB**: 모바일/웹/SaaS/핀테크/소셜/AI/게임, 시대별(2000s→2024+)·스펙트럼별 태깅
- **100+ 비유 라이브러리**: 그림이 그려지는 비유 (Fitts=양궁 과녁, Hick=식당 메뉴판, Peak-End=영화 결말)
- **하류 연계**: `ui-action-designer`(UI 스펙) 또는 `design-skill`(시각화) 핸드오프

## 연동 스킬

- **[ui-action-designer](https://github.com/jasonnamii/ui-action-designer)** — 스펙트럼 선택 후 실제 UI 설계 (Action/Task/SHE/PRD)
- **[design-skill](https://github.com/jasonnamii/design-skill)** — 선택 방향을 HTML/시각화로 바로 출력
- **[hit-skill](https://github.com/jasonnamii/hit-skill)** — 🟥 혁명 답변의 임팩트 증폭
- **[human-skill](https://github.com/jasonnamii/human-skill)** — 사용자 심리 근거 심층 보강
- **[triz](https://github.com/jasonnamii/triz)** — 혁명 설계의 모순 돌파
- **[research-frame](https://github.com/jasonnamii/research-frame)** — 니치 도메인 최신 리서치

## 설치

```bash
git clone https://github.com/jasonnamii/ux-advisor.git ~/.claude/skills/ux-advisor
```

## 업데이트

```bash
cd ~/.claude/skills/ux-advisor && git pull
```

`~/.claude/skills/` 에 둔 스킬은 Claude Code·Cowork 세션에서 자동으로 사용 가능합니다.

## 라이선스

MIT
