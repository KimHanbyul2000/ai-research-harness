"""판정 기준 개정 후 전수 재선별 — 분석 드라이버 (예시).

설계는 같은 폴더 `00_설계목표.md`, 결과는 `01_결과해석.md`.
재현: python out/20260101_판정기준개정_전수재선별/run.py

⚠ 이 파일은 예시다. `lib.analysis` 는 이 저장소에 없으며,
   골격이 어떤 모양인지 보여주기 위한 것이다. 값도 전부 가상이다.
"""

from pathlib import Path

# from lib.analysis import classify, load_units, save_csv

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data"

# ── 설계목표의 "정한 것" 표와 값이 일치한다 ──────────────────────
CRITERIA = {
    "theta": 0.0,
    "k": 10,
    "window_a": (302.5, 397.5),   # 개정된 경계
    "window_b": (397.5, 597.5),
}

# 구 경계 — 검산에만 쓴다. 판정에는 쓰지 않는다.
OLD_CRITERIA = {
    **CRITERIA,
    "window_a": (303.0, 419.0),
    "window_b": (419.0, 613.0),
}

# 2025-12-10 확정 결론. 검산의 기준값.
PREVIOUS_RESULT = {
    "U-0548", "U-0568", "U-0632", "U-1055", "U-1085", "U-1350",
}

SENSITIVITY_MS = 25.0   # 경계 직후 이 구간의 사건을 센다


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # units = load_units(n=3000, seed=42)     # 새로 측정하지 않는다

    # ── 검산: 구 경계로 돌리면 이전 결론이 재현되는가 ────────────
    # 경계만 바꿨다고 생각했는데 다른 것도 함께 바뀐 경우를 여기서 잡는다.
    #
    # reproduced = {u.id for u in classify(units, OLD_CRITERIA) if u.confirmed}
    # assert reproduced == PREVIOUS_RESULT, (
    #     f"구 경계 재현 실패 — 경계 외의 무언가가 함께 바뀌었다\n"
    #     f"  기대: {sorted(PREVIOUS_RESULT)}\n"
    #     f"  실제: {sorted(reproduced)}"
    # )

    # ── 본 판정: 3,000개 전수 ────────────────────────────────────
    # result = classify(units, CRITERIA)

    # ── 탈락분까지 전부 저장 ─────────────────────────────────────
    # 통과분만 저장하면 다음에 기준이 바뀔 때 3,000개를 다시 돌려야 한다.
    # 어느 단계에서 왜 떨어졌는지를 열로 남긴다.
    #
    # save_csv(DATA_DIR / "전수재선별.csv", result, columns=[
    #     "유닛", "그룹", "성립수", "판정", "탈락단계", "탈락사유",
    # ])

    # ── 취약성: 경계 직후 사건 수 ────────────────────────────────
    # 결론이 소수 사건에 걸려 있는 유닛을 드러낸다.
    #
    # save_csv(DATA_DIR / "경계민감도.csv", sensitivity(result, SENSITIVITY_MS))

    print(f"완료 — {DATA_DIR}")


if __name__ == "__main__":
    main()
