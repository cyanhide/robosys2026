# 階段ダイエットコマンド

![test](https://github.com/cyanhide/robosys2026/actions/workflows/test.yml/badge.svg)

本プログラムは、お昼ご飯で摂取したカロリー量を入力すると、階段の昇降によってそのカロリーを消費するために必要な運動量を計算し、何階まで登ればよいか、また必要に応じて何階まで下りる必要があるかを出力するプログラムである。

階段を1段登るごとに0.1Kcal、1段下りるごとに0.05Kcalを消費するものとし、1階あたり20段、最大19階まで昇ることができる条件を想定している。

## 使用方法と例

1.システムにPython 3がインストールされていることを確認してください。

2. 以下のコマンドを使用して実行してください。

(例）

```bash
$ seq 5 | ./plus
``` 

15

## インストール
GitHubからリポジトリをクローンする。

```bash
$ git clone https://github.com/cyanhide/robosys2023.git
```
クローン出来たらリポジトリのディレクトリに移動する
```bash
$ cd robosys2023
```


## 必要なソフトウェア

* python

   ◦テスト済み:3.7~3.10

## テスト環境

* Ubuntu 20.04 on Windows

## Licence
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは, 下記のスライド (CC-BY-SA 4.0 by Ryuichi Ueda) のものを, 本人の許可を得て自身の著作としたものです.
    * [ryuichiueda/my_slides robosys_2022 lesson4.md](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson4.md?plain=1)
* © 2023 Hidenori Koseki

