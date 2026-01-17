#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Hidenori Koseki
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "NG at Line $1"
    res=1
}

res=0


### 登りだけで足りる場合
# 1フロア登り = 2.0Kcal
out=$(echo 3 | ./stair_calorie.py)
[ "${out}" = "1階から3階まで階段を上ってください。" ] || ng ${LINENO}


### ちょうど19階まで登る場合
out=$(echo 36 | ./stair_calorie.py)
[ "${out}" = "1階から19階まで階段を上ってください。" ] || ng ${LINENO}


### 登り＋下りだけで済む場合
# 登り36Kcal + 下り5Kcal = 41Kcal
out=$(echo 40 | ./stair_calorie.py)
[ "${out}" = "1階から19階まで階段を上り、19階から14階まで降りてください。" ] || ng ${LINENO}


### 往復だけで済む場合
# 1往復 = 36 + 18 = 54Kcal
out=$(echo 54 | ./stair_calorie.py)
[ "${out}" = "往復1セット（登り＋下り）してください。" ] || ng ${LINENO}


### 往復＋登りの場合
out=$(echo 60 | ./stair_calorie.py)
[ "${out}" = "往復1セット（登り＋下り）と、1階から4階まで階段を上ってください。" ] || ng ${LINENO}


### 文字入力
out=$(echo あ | ./stair_calorie.py)
[ "$?" = 1 ]      || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}


### 記号入力
out=$(echo . | ./stair_calorie.py)
[ "$?" = 1 ]      || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}


### 空入力
out=$(echo | ./stair_calorie.py)
[ "$?" = 1 ]      || ng ${LINENO}
[ "${out}" = "" ] || ng ${LINENO}


### 結果
[ "$res" = 0 ] && echo OK
exit $res
