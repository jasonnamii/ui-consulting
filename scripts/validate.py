#!/usr/bin/env python3
"""
ux-advisor self-check
스킬 수정 후 구조적 무결성 검증. 의미 판정은 skill-doctor 몫.

실행: python scripts/validate.py
종료 코드: 0=PASS, 1=FAIL
"""
import json
import re
import sys
from pathlib import Path


def check_skill_md(skill_md_path: Path) -> list[str]:
    """SKILL.md 구조 체크. 실패 사항 목록 반환."""
    errors: list[str] = []
    if not skill_md_path.exists():
        return ["SKILL.md 없음"]

    text = skill_md_path.read_text(encoding="utf-8")

    # 1. frontmatter에 version
    if not re.search(r"^version:\s*\d+\.\d+\.\d+", text, re.MULTILINE):
        errors.append("frontmatter version 필드 없음")

    # 2. 절대 규칙 섹션 존재
    if "## 절대 규칙" not in text:
        errors.append("'절대 규칙' 섹션 없음")

    # 3. 4단계 이모지 모두 언급
    for emoji in ["🟦", "🟩", "🟨", "🟥"]:
        if emoji not in text:
            errors.append(f"4단계 이모지 {emoji} 본문에 없음")

    # 4. 3요소 키워드
    for keyword in ["원리", "이론", "사례", "비유"]:
        if keyword not in text:
            errors.append(f"3요소 키워드 '{keyword}' 없음")

    # 5. 🟥 리스크 병기 규칙
    if "리스크" not in text:
        errors.append("🟥 리스크 병기 규칙 언급 없음")

    # 6. Gotchas 섹션
    if "## Gotchas" not in text:
        errors.append("Gotchas 섹션 없음")

    # 7. 크기 경고(하드 실패 아님)
    size = len(text.encode("utf-8"))
    if size > 10_000:
        errors.append(f"SKILL.md 크기 {size}B > 10KB (경고)")

    return errors


def check_evals(evals_dir: Path) -> list[str]:
    """evals/cases.json 구조 체크."""
    errors: list[str] = []
    cases_path = evals_dir / "cases.json"
    if not cases_path.exists():
        return ["evals/cases.json 없음"]

    try:
        data = json.loads(cases_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"cases.json JSON 파싱 실패: {e}"]

    cases = data.get("cases", [])
    if len(cases) < 3:
        errors.append(f"케이스 수 {len(cases)} < 3 (최소 기준)")

    required_fields = {"id", "category", "input", "expect"}
    for i, case in enumerate(cases):
        missing = required_fields - set(case.keys())
        if missing:
            errors.append(f"case[{i}] 누락 필드: {missing}")

    return errors


def check_references(references_dir: Path) -> list[str]:
    """references/ 필수 파일 존재 체크."""
    errors: list[str] = []
    required = [
        "protocol.md",
        "spectrum-map.md",
        "domain-lens.md",
        "research-1-theories.md",
        "research-2-cases.md",
        "research-3-revolutions-and-analogies.md",
    ]
    for fname in required:
        if not (references_dir / fname).exists():
            errors.append(f"references/{fname} 없음")
    return errors


def main() -> int:
    skill_root = Path(__file__).resolve().parent.parent

    print(f"[ux-advisor validate] root: {skill_root}")

    all_errors: list[str] = []
    all_errors += [f"[SKILL.md] {e}" for e in check_skill_md(skill_root / "SKILL.md")]
    all_errors += [f"[evals] {e}" for e in check_evals(skill_root / "evals")]
    all_errors += [f"[references] {e}" for e in check_references(skill_root / "references")]

    if all_errors:
        print(f"\n🔴 FAIL ({len(all_errors)}건)")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print("\n🟢 PASS — 구조 무결성 확인. 의미 판정은 skill-doctor 실행 권장.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
