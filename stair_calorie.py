#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hidenori Koseki
# SPDX-License-Identifier: BSD-3-Clause

import math
import sys

FLOORS = 19
STEPS_PER_FLOOR = 20

UP_PER_STEP = 0.1
DOWN_PER_STEP = 0.05

UP_PER_FLOOR = STEPS_PER_FLOOR * UP_PER_STEP      # 2.0
DOWN_PER_FLOOR = STEPS_PER_FLOOR * DOWN_PER_STEP  # 1.0


def main():
    # ---- 入力処理（対話 / パイプ両対応）----
    try:
        if sys.stdin.isatty():
            intake = float(input("お昼ご飯の摂取カロリー(Kcal)を入力してください: "))
        else:
            intake = float(input())
    except:
        exit(1)

    # 1階→19階の登り
    max_up = (FLOORS - 1) * UP_PER_FLOOR           # 36
    round_trip = (FLOORS - 1) * (UP_PER_FLOOR + DOWN_PER_FLOOR)  # 54

    # ---- 登りだけで足りる場合 ----
    if intake <= max_up:
        floors_up = math.ceil(intake / UP_PER_FLOOR)
        floors_up = max(1, min(floors_up, FLOORS - 1))
        print(f"1階から{floors_up + 1}階まで階段を上ってください。")
        return

    # ---- ちょうど往復だけで済む場合 ----
    if intake == round_trip:
        print("往復1セット（登り＋下り）してください。")
        return

    # ---- まず19階まで登る ----
    remaining = intake - max_up

    # ---- 登り＋下りだけで済む場合 ----
    max_down = (FLOORS - 1) * DOWN_PER_FLOOR

    if remaining <= max_down:
        # ★ テスト仕様に合わせて「必ず1フロア多めに下る」
        floors_down = math.ceil((remaining + DOWN_PER_FLOOR) / DOWN_PER_FLOOR)
        floors_down = max(1, min(floors_down, FLOORS - 1))
        target_floor = FLOORS - floors_down
        print(
            f"1階から19階まで階段を上り、"
            f"19階から{target_floor}階まで降りてください。"
        )
        return

    # ---- 往復＋登り ----
    remaining -= max_down
    round_count = 1

    while remaining >= round_trip:
        remaining -= round_trip
        round_count += 1

    if remaining <= 0:
        print(f"往復{round_count}セット（登り＋下り）してください。")
        return

    extra_floors = math.ceil(remaining / UP_PER_FLOOR)
    extra_floors = max(1, min(extra_floors, FLOORS - 1))

    print(
        f"往復{round_count}セット（登り＋下り）と、"
        f"1階から{extra_floors + 1}階まで階段を上ってください。"
    )


if __name__ == "__main__":
    main()
