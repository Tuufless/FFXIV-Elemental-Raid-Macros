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

The following is [Waun Siu's macro](https://jp.finalfantasyxiv.com/lodestone/character/15557346/blog/5090419/), which has been the base for P8S prog in JP.

### Japanese

```
■テトラ頭割り　|　■オクタ散開
D3MT　 STD4   |　　D3　D4
　　　★　　　   |　　MT　ST
H1D1　H2D2   |　　　  ★
　　　　　　　   |        D1　D2
　　　　　　　   |        H1　H2
-----------１回目-------------------------
◎腕蛇形態
■蛇担当 
12時から反時計>MTD1>STD2>H1D3>H2D4>1時から時計
◎脚獣形態
■岩散開　　| ■フェイタルストンプ
D3 MT D4　|  1(奇数)  A(待機)　※1マーカーとMAP中央で
H1 H2  ST　|　　　　  ★(偶数)　　 交互に飛ばす
D1        D2　|　　　　　　　　　 　 待機はA
----------------------------------------------------
◎幻影創造
■4方向直線攻撃　   |   ■8方向散開
MT(D3) 　ST(D4)   |　　MT　ST 
　　　　★　　　　  | D3　　　　 D4
H1(D1)　 H2(D2)  |　　　  ★
　　　　　　　　　  | H1　 　　　H2
　　　　　　　　　  |　　D1　D2
◎四重炎嵐
■2回目安置が角の場合
西:MTH1D13　　東:ST2H2D24
■散開 &頭割　　　■角テトラ
↑↑ボス↑↑　　　　内T近接　外H遠隔
MTD1    D2ST　　 ■角オクタ
D3H1   H2D4 　　　　近　　  ※近が中央側
　　　　　　　　　　T　　遠
　　　　　　　　　　    H　　　
沼消えてからの
鳥or竜＋散開or頭割りは開幕の位置へ戻って処理
-----------2回目---------------------
◎腕蛇形態
■蛇担当
D3 MT D4　※MTD3/STD4/H1D1/H2D2
H1  ★   ST　　 ペアで担当の場所を処理
D1 H2 D2
■ペトリアイ＋頭割り
TH/DPSそれぞれデバフ有り同士、無し同士で優先度移動
12時から反時計>MTD1>STD2>H1D3>H2D4>1時から時計
◎脚獣形態
■テトラ(2222頭割り)　■ディフレア(44頭割り)
ボスから　　　　　　　　ボス側:MTH1D1D2
MTD1　　　　　　 　　  遠い側: STH2D3D4
 STD2
H1D3
H2D4
```

## English

```
■ Tetraflare  　|　■ Octaflare
D3MT　 STD4   |　　D3　D4
　　　★　　　   |　　MT　ST
H1D1　H2D2   |　　　  ★
　　　　　　　   |        D1　D2
　　　　　　　   |        H1　H2
----------- Reforged Reflection #１-------------------------
◎ Snake-arm form
■ Eye/Blood of the Gorgon priority
　CCW from 12 o'clock：MTD1>STD2>H1D3>H2D4：CW from 1 o'clock
◎ Beast-leg form
■ AoE Spread| ■ Stomp Dead (L-stomps)
D3 MT D4　|  1(odd)  A(standby)　※ Standby
H1 H2  ST　|　　　　  ★(even)　　 　　at A
D1        D2　| 　Alternate stomps 1←→mid
----------------------------------------------------
◎ Illusory Creation
■ Nest of Flamevipers (4x line attack, 8-man spread)
MT(D3) 　ST(D4)   |　　MT　ST 
　　　　★　　　　  | D3　　　　 D4
H1(D1)　 H2(D2)  |　　　  ★
　　　　　　　　　  | H1　 　　　H2
　　　　　　　　　  |　　D1　D2
◎ Fourfold Fires
■ 2 corner safe-spots
West: MTH1D1D3　East: ST2H2D2D4
■ Spread & Stack　■ Corner Tetraflare
↑↑Boss↑↑　　　　In：T+M　Out：H+R
MTD1    D2ST　　　■ Corner Octaflares
D3H1   H2D4 　　　　M　　  ※ Melee towards mid
　　　　　　　　　　T　　R
　　　　　　　　　　    H　　　
After puddles disappear：
　Return to opener positions to resolve
　Phoenix/dragon＋stack/spread
----------- Reforged Reflection #2---------------------
◎ Snake-arm form
■ Blood/Eye of the Gorgon
D3 MT D4　※ Resolve in pairs:
H1  ★   ST　　 MTD3/STD4/H1D1/H2D2
D1 H2 D2
■ Cursed Shriek + Breath of the Gorgon stacks
TH/DPS debuff/no-debuff pair priority：
　CCW from 12 o'clock：MTD1>STD2>H1D3>H2D4：CW from 1 o'clock
◎ Beast-leg form
■ Tetraflare (2222 stacks)　■ Diflare(4:4 stacks)
From boss　　　　　　　Boss side:MTH1D1D2
MTD1　　　　　　 　　  Far side: STH2D3D4
 STD2
H1D3
H2D4
```

## Markers

These markers are for Waun's Siu's macro.

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