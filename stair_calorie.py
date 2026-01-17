#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hidenori Koseki
# SPDX-License-Identifier: BSD-3-Clause

import sys
import math

FLOORS = 19
STEPS_PER_FLOOR = 20

UP_PER_STEP = 0.1
DOWN_PER_STEP = 0.05

UP_PER_FLOOR = STEPS_PER_FLOOR * UP_PER_STEP      # 2.0 Kcal
DOWN_PER_FLOOR = STEPS_PER_FLOOR * DOWN_PER_STEP  # 1.0 Kcal


def main():
    try:
        if sys.stdin.isatty():
            intake = float(input("お昼ご飯の摂取カロリー(Kcal)を入力してください: "))
        else:
            intake = float(input())
    except:
        exit(1)

    remaining = intake

    max_up = (FLOORS - 1) * UP_PER_FLOOR
    round_trip = (FLOORS - 1) * (UP_PER_FLOOR + DOWN_PER_FLOOR)

    # ── 登りだけで足りる場合 ──
    if remaining <= max_up:
        floors_up = math.ceil(remaining / UP_PER_FLOOR)
        floors_up = max(1, min(floors_up, FLOORS - 1))
        print(f"1階から{floors_up + 1}階まで階段を上ってください。")
        return

    # ── まず1回は19階まで登る ──
    remaining -= max_up

    # ── 下りだけで済むか判定 ──
    max_down = (FLOORS - 1) * DOWN_PER_FLOOR
    if remaining <= max_down:
        floors_down = math.ceil(remaining / DOWN_PER_FLOOR)
        floors_down = max(1, min(floors_down, FLOORS - 1))
        target_floor = FLOORS - floors_down
        print(
            f"1階から19階まで階段を上り、"
            f"19階から{target_floor}階まで降りてください。"
        )
        return

    # ── 往復処理 ──
    remaining -= max_down
    round_count = 1

    while remaining >= round_trip:
        remaining -= round_trip
        round_count += 1

    # ── 往復だけで済む場合 ──
    if remaining <= 0:
        print(f"往復{round_count}セット（登り＋下り）してください。")
        return

    # ── 往復＋追加の登り ──
    extra_floors = math.ceil(remaining / UP_PER_FLOOR)
    extra_floors = max(1, min(extra_floors, FLOORS - 1))

    print(
        f"往復{round_count}セット（登り＋下り）と、"
        f"1階から{extra_floors + 1}階まで階段を上ってください。"
    )


if __name__ == "__main__":
    main()
