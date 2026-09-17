"""<주제> — 분석 드라이버.

설계는 같은 폴더 `00_설계목표.md`, 결과는 `01_결과해석.md`.
재현: python out/<이 폴더>/run.py

이 파일은 '조립'만 한다. 재사용 가능한 계산은 lib/ 에서 import하고,
여기에는 "어떤 값으로 어떤 순서로 불렀는가"만 남긴다.
"""

from pathlib import Path

# from lib.analysis import classify, load        # 승격된 계산만 import

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data"        # 출력 경로를 자기 폴더로 명시 지정한다
FIG_DIR = HERE / "figures"      # 기본값에 의존하지 않는다

# ── 설계목표의 "정한 것" 표와 값이 일치해야 한다 ──────────────────
CRITERIA = {
    # "threshold": 0.0,         # 이유는 00_설계목표.md 에 적혀 있다
}

# 이전 분석의 확정 결론. 재현 검산의 기준값.
PREVIOUS_RESULT: set = set()
OLD_CRITERIA: dict = {}


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    # data = load(...)

    # ── 재현 검산 ────────────────────────────────────────────────
    # 판정 기준을 바꿔 다시 돌리는 분석이라면, 옛 기준으로 이전 결론이
    # 그대로 나오는지 먼저 단언한다. 기준만 바꿨다고 생각했는데 다른
    # 것도 함께 바뀐 경우를 여기서 잡는다.
    #
    # assert set(classify(data, OLD_CRITERIA)) == PREVIOUS_RESULT, (
    #     "옛 기준 재현 실패 — 기준 변경 외의 무언가가 함께 바뀌었다"
    # )

    # ── 본 판정 ──────────────────────────────────────────────────
    # result = classify(data, CRITERIA)

    # ── 탈락분까지 전부 저장한다 ─────────────────────────────────
    # 통과분만 저장하면 기준이 바뀔 때 전체를 다시 계산해야 한다.
    # 어느 단계에서 떨어졌는지를 열로 남긴다.
    #
    # save_csv(DATA_DIR / "판정결과.csv", result, columns=[
    #     "대상", "지표", "판정", "탈락단계", "탈락사유",
    # ])

    print(f"완료 — {DATA_DIR}")


if __name__ == "__main__":
    main()
