# 階段ダイエットコマンド

![test](https://github.com/cyanhide/robosys2026/actions/workflows/test.yml/badge.svg)

本プログラムは、お昼ご飯で摂取したカロリー量を入力すると、階段の昇降によってそのカロリーを消費するために必要な運動量を計算し、何階まで登ればよいか、また必要に応じて何階まで下りる必要があるかを出力するプログラムである。

階段を1段登るごとに0.1Kcal、1段下りるごとに0.05Kcalを消費するものとし、1階あたり20段、最大19階まで昇ることができる条件を想定している。

## 実行例
①
```
$ ./stair_calorie.py
お昼ご飯の摂取カロリー(Kcal)を入力してください: 130 
往復2セット（登り＋下り）と、1階から12階まで階段を上ってください。
```
②
```
$ echo 130 | ./stair_calorie.py
往復2セット（登り＋下り）と、1階から12階まで階段を上ってください。
```

## インストール方法
* pythonが導入された環境で, 下記のコマンドを入力する。
```
$ git clone https://github.com/cyanhide/robosys2026.git
```
* robosys2026ディレクトリに移動。
```
$ cd robosys2026
```
* 実行方法に関しては、上記の使い方を参照してください。実行権限が付与されていない場合は, 下記コマンドを入力してください。
```
$ chmod +x stair_calorie.py
```

## 必要なソフトウェア

* python

   ◦テスト済み:3.7~3.10
* Ubuntu 20.04.4 LTS

## テスト環境

* Ubuntu 20.04.4 LTS

## Licence
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* © 2025 Hidenori Koseki
## 参考文献
- このパッケージのディレクトリ構成やテスト方式、コードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て参考にしています。
    - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025) （© 2025 Ryuichi Ueda）
