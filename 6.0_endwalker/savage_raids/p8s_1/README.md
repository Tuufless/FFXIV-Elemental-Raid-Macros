---
layout: default
title: P8S P1
parent: Savage Raids
nav_order: "08_1"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p8s_1/
---

# Abyssos: The Eighth Circle (Savage) - Part 1

**DISCLAIMER:** *I haven't gotten around to clearing P8S myself yet, so I may be missing some context in the translation below.*

### Things to check on Party Finger

- Check the Gorgons priority system- there are several different priorities going around, **even between the two sets of macros below.**

### Japanese

[Game8](https://game8.jp/ff14/480095) went along with the macro for the [FFO strat](https://jp.finalfantasyxiv.com/lodestone/character/17170591/blog/5094725/).

The following videos specifically go over the FFO strat:

  - [Hamkatsu](https://youtu.be/D63JWdvXqWY)
  - [Inumaru](https://youtu.be/YSRmSAbPyAM)

```
■テトラオクタ/誘導/蛇2　 ■基本散会
　MT/D3　→　ST/D4　　　D3 MT D4
　　↑　　 ☆　　↓　 　　　H1(H2) ST
　H1/D1　←　H2/D2 　　D1 H2 D2
■イントゥシャドウ(1回目)
　蛇：北から時計回りMTD1>STD2>H1D3>H2D4
■フェイタルストンプ
　1,3回目→1(北西)　2,4回目→中央　待機→A(北)
■幻影創造
◎竜竜×散開　　　　 │◎フェニ×散開
　　　　D3　　　 　 │　D3 MT D4
　　　　MT　ST　D4│　H1 ☆ ST
　　H1 D1　D2　　 │　D1 H2 D2
　　　　　　 H2　　 │
■四重炎嵐(縦横) ｜■四重炎嵐(角)
　　　 MT　　　│　　中央　※MT組：西優先
　 D1 ST D2 ｜T　近
　D3 H1 H2 D4 │遠 H
◎頭割り：近H位置(MTD1/STD2/H1D3/H2D4)
■イントゥシャドウ(2回目) 4:4頭割り
　デバフ持ち：北西>MT/D1>ST/D2>H1/D3>H2/D4>南東
　無職：北西TH/南東DPS
■テトラ/ディフレア
　テトラ：(ボス)MT/D1>ST/D2>H1/D3>H2/D4
　ディフレア：(ボス)MTH1D1D2>STH2D3D4 
```

### English

```
■Tetra/Octa/baits/Snakes 2　 ■ Basic Spread
　MT/D3　→　ST/D4　　　　　　  D3 MT D4
　　↑　　 ☆　　↓　　　　　　　　H1(H2) ST
　H1/D1　←　H2/D2　　　　　　 D1 H2 D2
■ Into the Shadows #1
　Gorgons：From N, going clockwise
　　　MTD1>STD2>H1D3>H2D4
■ Stomp Dead
　1st, 3rd→NW　2nd, 4th→mid　Standby→N
■ Illusory Creation
◎2x Dragon + spread│◎ 2x Phoenix + spread
　　　　D3　　　 　 　│　D3 MT D4
　　　　MT　ST　D4   │　H1 ☆  ST
　　H1 D1　D2　　　 │　D1 H2 D2
　　　　　　 H2　　 　│
■Fourfold Fires(sides) ｜■Fourfold Fires(corners)
　　　　　 MT　　　　　│　　mid　※MT group：
　　　 D1 ST D2 　　　   ｜　T　M　　　West priority
　　D3 H1 H2 D4 　　　│　R　H
◎ Stacks：M+H locations (MTD1/STD2/H1D3/H2D4)
■ Into the Shadows #2 (4:4 stacks)
　Debuffs：NW：MT/D1>ST/D2>H1/D3>H2/D4：SE
　Nothing：NW→TH　SE→DPS
■ Tetraflare/Diflare
　Tetraflare：(Boss)MT/D1>ST/D2>H1/D3>H2/D4
　Diflare：(Boss)MTH1D1D2>STH2D3D4 
```

## Markers

- 1 and A are for resolving Stomp Dead (using the L-stomp method)

![](images/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"P8S","MapID":884,"A":{"X":100.0,"Y":0.0,"Z":91.6,"ID":0,"Active":true},"B":{"X":108.4,"Y":0.0,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.0,"Z":108.4,"ID":2,"Active":true},"D":{"X":91.6,"Y":0.0,"Z":100.0,"ID":3,"Active":true},"One":{"X":91.6,"Y":0.0,"Z":91.6,"ID":4,"Active":true},"Two":{"X":108.4,"Y":0.0,"Z":91.6,"ID":5,"Active":true},"Three":{"X":108.4,"Y":0.0,"Z":108.4,"ID":6,"Active":true},"Four":{"X":91.6,"Y":0.0,"Z":108.4,"ID":7,"Active":true}}
```

</details>

## L-Stomps

"L-Stomps" refers to the following Tweet:

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">4層前半のフェイタルストンプ(ピョンピョンするやつ)近接ずっと殴れるやり方<br>(うちの学者さん考案)<br>これめっちゃいい <a href="https://t.co/wQWMBX5olX">pic.twitter.com/wQWMBX5olX</a></p>&mdash; あおいさまさま (@aoisamasama23) <a href="https://twitter.com/aoisamasama23/status/1565394643763597312?ref_src=twsrc%5Etfw">September 1, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

This is a way to resolve the Earth AoEs and the "Stomp Dead" mechanic in the first "beast" mode.

Note that the video in the Tweet uses the `A` and `2` markers to resolve the mechanic, while the macro uses `1` and `A` instead.

![](images/stomp_dead.jpg)
*(Credit: [Berga Thompson](https://jp.finalfantasyxiv.com/lodestone/character/17170591/blog/5094725/))*

## Illusory Creation

In the event the boss uses Nest of Flamevipers when the clones are 2x Dragons, the spread positions are as follows:

![](images/illusory_creation_dragon_spread.jpg)
*(Credit: [Berga Thompson](https://jp.finalfantasyxiv.com/lodestone/character/17170591/blog/5094725/))*

## Fourfold Fires

Here is how to handle the stacks/spreads in Fourfold Fires.

**Note that the corner spreads here are the FFO strat's spread positions, and are different from Waun Siu's strat.**

<table>
  <tr>
    <td><img src="images/fourfold_fires_sides_spreads.jpg"></td>
    <td><img src="images/fourfold_fires_sides_stacks.jpg"></td>
  </tr>
  <tr>
    <td><img src="images/fourfold_fires_corners_spreads.jpg"></td>
    <td><img src="images/fourfold_fires_corners_stacks.jpg"></td>
  </tr>
</table>

*(Credit: [Berga Thompson](https://jp.finalfantasyxiv.com/lodestone/character/17170591/blog/5094725/))*

## Into the Shadows #2 (4:4 stacks)

![](images/gorgon_2.jpg)
*(Credit: [Berga Thompson](https://jp.finalfantasyxiv.com/lodestone/character/17170591/blog/5094725/))*