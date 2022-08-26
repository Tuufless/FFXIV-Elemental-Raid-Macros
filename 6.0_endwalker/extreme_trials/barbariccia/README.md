---
layout: default
title: Barbariccia EX
parent: Extreme Trials
nav_order: 4
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/extreme_trials/barbariccia/
---

# Storm's Crown (Extreme)

This is [game8's macro](https://game8.jp/ff14/477950).

It's basically [Hamkatsu's strat](https://youtu.be/e-w4nFwWw-8), but resolves Playstation symbols in a "braindead" manner (T/H go to assigned cardinals, DPS all stack in the center and get pulled to their assigned partner). 

## Japanese
```
【散開基準】ヘアレイド：ボス基準　それ以外：北基準
【基本散開】　 【ペア塔】
D3 MT D4　　　MTD3
H1　　H2　 H1D1　 H2D4
D1 ST D2　 　　 STD2
【ヘアレイド】H1 MT ◎ ST H2
　　　　　　　D3 D1　D2 D4
【距離減衰+頭割り】【プレステ脳死】
　　MT　　ST　　　　　　MT
　　　　◎ 　 　 　　　H1 DPS H2
　　　頭割り 　 　 　　　　ST　※マーカー問わずDPS中央
【呪髪拘束1回目】ペア塔：① ③マーカー付近 AOE：ペア塔と逆
【4連円範囲捨て】Cマーカー付近スタートで時計回り
【呪髪拘束2回目】DPS：時計回り側　TH：反時計回り側
```

## English
```
Hair Raid：Boss-relative　Others：Map-relative
【Spread】　　 【Pairs】
　D3 MT D4　　　MTD3
　H1　　H2　 H1D1　 H2D4
　D1 ST D2　 　　 STD2
【Hair Raid】H1 MT ◎ ST H2
　　　　　　　D3 D1　D2 D4
【2x Flares + stack】【Playstation (braindead)】
　　MT　　ST　　　　　　　　MT
　　　　◎ 　 　 　　　　　H1 DPS H2
　　　stack 　 　　　 　　　　  ST
【Teasing Tangles #1】Pairs at ①+③
【Mario Kart】Start at C, run clockwise
【Teasing Tangles #2】DPS：cw　TH：ccw
```

## Markers

You might see the `ABCD` markers placed further out towards the edge of the arena.

- `ABCD`: Orientation, T/H Playstation positions
- `C`: Party stack during 2x Flares + stack
- `1` and `3`: Enumeration pairs during Teasing Tangles

![](images/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"Barbariccia EX","MapID":871,"A":{"X":100.0,"Y":0.0,"Z":91.5,"ID":0,"Active":true},"B":{"X":108.5,"Y":0.0,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.0,"Z":108.5,"ID":2,"Active":true},"D":{"X":91.5,"Y":0.0,"Z":100.0,"ID":3,"Active":true},"One":{"X":106.0,"Y":0.0,"Z":94.0,"ID":4,"Active":true},"Two":{"X":106.0,"Y":0.0,"Z":94.0,"ID":5,"Active":false},"Three":{"X":94.0,"Y":0.0,"Z":106.0,"ID":6,"Active":true},"Four":{"X":94.0,"Y":0.0,"Z":106.0,"ID":7,"Active":false}}
```
</details>
