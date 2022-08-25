---
layout: default
title: Barbariccia EX
parent: Extreme Trials
nav_order: 4
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/extreme_trials/barbariccia/
---

# Storm's Crown (Extreme)

PF largely follows [Hamkatsu's strat](https://youtu.be/e-w4nFwWw-8).

### Things to check on Party Finder

Check the Enumeration pairs- some macros pair MTD4, H2D2, ... instead of MTD3, H2D4, ...

## English
```
■ Spread　　■ Playstation
　D3 MT D4　　　　△
　H1　　H2　　□　　　○
　D1 ST  D2　　　　×
【4:4 stacks】D3 H1 D1 MT←→ST D2 H2 D4
【Hair+AoE+Enumeration】NE + SW
【Enumeration Pairs】MTD3　H2D4　STD2　H1D1
【Mario Kart】Start South, run cw
【2x Flares + stack】MT→NW　ST→NE　stack→S
【PS1 spread】DPS→cw　T/H→ccw
【PS2 pairs】Pairs without Enums rotate cw
　unless both Enum pairs are next to each other
```

## Japanese
```
■基本散開　　■プレステ散開
　D3 MT D4　　　　△
　H1　　H2　　□　　　○
　D1 ST  D2　　　　×
【4:4頭割り】D3 H1 D1 MT←→ST D2 H2 D4
【ヘアレイド足元】ボス向き基準で散開or頭割り
【髪+AoE+頭割り】北東(1マーカー)と南西（3マーカー）で頭割り
【タコマーカー】中央に捨て方角基準で基本散開
【ペア頭割り】MTD3　H2D4　STD2　H1D1
【線+エラプ】南スタート　時計回り
【フレア+頭割り】MT北西　ST北東　頭割り南
【プレステ後散開】AoE跨ぎDPS時計側、TH反時計側
【ペア頭割り】無職組が時計移動
　　　　　　　無職が被る場合のみ片方が反時計移動
```

## Markers

Note that the `ABCD` markers aren't all the way at the edge- this is to make them easier to spot when the boss transforms and the arena shrinks.

- `ABCD`: Orientation
- `C`: Party stack during 2x Flares + stack
- `1` and `3`: Enumeration pairs during Teasing Tangles

![](images/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"Barbariccia EX","MapID":871,"A":{"X":100.0,"Y":0.0,"Z":87.0,"ID":0,"Active":true},"B":{"X":113.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.0,"Z":113.0,"ID":2,"Active":true},"D":{"X":87.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},"One":{"X":106.0,"Y":0.0,"Z":94.0,"ID":4,"Active":true},"Two":{"X":0.0,"Y":0.0,"Z":0.0,"ID":5,"Active":false},"Three":{"X":94.0,"Y":0.0,"Z":106.0,"ID":6,"Active":true},"Four":{"X":0.0,"Y":0.0,"Z":0.0,"ID":7,"Active":false}}
```
</details>
