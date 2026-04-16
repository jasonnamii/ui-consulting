# ux-advisor

🇰🇷 [한국어 README](./README.ko.md)

**UX consultation engine that answers any UX question across a 4-tier spectrum (Conservative · Standard · Progressive · Revolutionary) — each grounded in theory, real-world cases, and memorable analogies.**

## Prerequisites

- **Claude Cowork or Claude Code** environment

## Goal

Most UX advice is either a single "best practice" or a vague "it depends." ux-advisor resolves this by giving you **four parallel answers** for every UX question, spanning decades of design evolution — from legacy patterns to category-redefining revolutions. Each answer combines a principle, real service examples, and a vivid analogy so decisions become tangible, not abstract.

## When & How to Use

Trigger it whenever you face a UX decision: onboarding flow, payment UX, navigation structure, notification design, feed architecture, error handling — anything where "how should we build this?" is the question. Ask in natural language ("payment cancellation UX 어떻게?") and get the full spectrum, then choose a direction to hand off to **ui-action-designer** (full UI design) or **design-skill** (direct visualization).

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| Design decision pending | `"결제 취소 UX 어떻게 해?"` | 4-tier answer with Toss/Amazon/Stripe case studies + analogies |
| Competitor analysis follow-up | `"온보딩 어떻게 짜지?"` | Conservative→Revolutionary spectrum (Windows→Slack→Duolingo→ChatGPT) |
| Strategic differentiation | `"피드 구조 추천해줘"` | Timeline vs algorithm vs hybrid vs FYP-style mapped to risk profile |
| Feature ideation | `"알림 설계 조언"` | Conservative push → standard DND → Slack-style → BeReal 1-per-day |

## Key Features

- **4-tier spectrum**: 🟦 Conservative (legacy) · 🟩 Standard (current mainstream) · 🟨 Progressive (mainstream + variation) · 🟥 Revolutionary (category redefinition)
- **3-element format**: Every answer has theory + real service names + memorable analogy — no abstract advice
- **80+ UX principles** embedded: Nielsen heuristics, Gestalt laws, Fitts/Hick/Miller/Tesler, behavioral economics, accessibility
- **130+ case studies**: Mobile/web/SaaS/fintech/social/AI/games, tagged by era (2000s→2024+) and spectrum position
- **100+ analogies**: Vivid mental pictures (Fitts = archery target, Hick = restaurant menu, Peak-End = movie ending)
- **Downstream chaining**: Hand off to `ui-action-designer` for UI specs or `design-skill` for visuals

## Works With

- **[ui-action-designer](https://github.com/jasonnamii/ui-action-designer)** — Actual UI design (Action/Task/SHE/PRD) after spectrum selection
- **[design-skill](https://github.com/jasonnamii/design-skill)** — Direct HTML/visual output for chosen direction
- **[hit-skill](https://github.com/jasonnamii/hit-skill)** — Amplifies impact of 🟥 Revolutionary answers
- **[human-skill](https://github.com/jasonnamii/human-skill)** — Deeper user psychology backing
- **[triz](https://github.com/jasonnamii/triz)** — Resolves contradictions in Revolutionary designs
- **[research-frame](https://github.com/jasonnamii/research-frame)** — Fresh research for niche domains

## Installation

```bash
git clone https://github.com/jasonnamii/ux-advisor.git ~/.claude/skills/ux-advisor
```

## Update

```bash
cd ~/.claude/skills/ux-advisor && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## License

MIT
