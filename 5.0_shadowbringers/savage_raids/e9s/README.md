---
layout: default
title: E9S
parent: Savage Raids
nav_order: "09"
grand_parent: 5.0 Shadowbringers
permalink: /5.0_shadowbringers/savage_raids/e9s/
---

# Eden's Promise: Umbra (Savage)

The standard PF strategy uses [Akito's strat (あきと式)](https://youtu.be/FMJ2W5_MLW8) as a base, but replaces the Empty Plane positions with Yamipika (やみぴか) positions, although you'll often see "天空近接内" instead (melees in for Empty Plane). Yamipika essentially ensures tanks and melee DPS have full uptime on the boss throughout the Empty Plane phase.

### Things to check on Party Finder

- Tower positions may be flipped horizontally.
- It's also worth checking the Empty Plane positions just to be sure.

## English
```
【Beam Spread】【Beam Pairs】
D3　MT　D4　　　 　 MTD3
H1　 ▲　 H2　 　H1D1 ▲ D4H2
D1　 OT　 D2 　 　　 　OTD2
ーーーーーーーーーーーーーーーーー
【Anti-air/Wide-angle】
D1D3H1　▼　D2D4H2
　　MT　　　　  OT
ーーーーーーーーーーーーーーーーー
　【Seeds】　　　 【Towers】
　H1 MT H2　 　    D4　　　D3
　D3  ▲   OT　 　 　 　D2 D1
　D1 D4 D2　 　 　 　OT MT
　TH→SW 　　　　H2　　　H1
　DPS→NE
ーーーーーーーーーーーーーーーーー
【Empty Plane】【十-positions】
　　　　　　　　 　　　D3
　MT D3 D2　　 　　　MT
　H1  ▲  H2　　H1 D1 ▲ D2 H2
　D1  D4 OT　　　　　 OT
　　　　　　　　 　　　 D4
ーーーーーーーーーーーーーーーーー
【Dodge West】【Dodge East】
　　　　  D3　　　　D3
　　  MT  D2　　 　　H1 MT
　H1 D1  ▲　　  　　 ▲  D2 H2
　　  OT  H2　　 　　D1 OT
　　　　  D4　　 　　D4
```

<details markdown=block>
<summary>Akito's Empty Plane</summary>

To replace Yamipika with Akito's original Empty Plane positions, swap in the following blocks. Note the melee positions in Empty Plane- they will disconnect from the boss when it comes to the 十-formation.

```
【Empty Plane】【十-positions】
　　　　　　　　 　　　D3
　H1 D3 MT　　 　　　MT
　D1  ▲  D2　　D1 H1 ▲ H2 D2
　OT  D4 H2　　　　　 OT
　　　　　　　　 　　　 D4
ーーーーーーーーーーーーーーーーー
【Dodge West】【Dodge East】
　　　　  D3　　　　D3
　　  MT  D2　　 　　H1 MT
　D1 H1  ▲　　  　　 ▲  H2 D2
　　  OT  H2　　 　　D1 OT
　　　　  D4　　 　　D4
```

</details>

## Japanese
```
【ビーム散開】　 　 【ビーム２受け】
D3　MT　D4　　　 　 MTD3
H1　 ▲　 H2　 　H1D1 ▲ D4H2
D1　 ST　 D2 　 　　 　STD2
ーーーーーーーーーーーーーーーーー
　【高射・広角】
D1D3H1　▼　D2D4H2
　　MT　　　　  ST
ーーーーーーーーーーーーーーーーー
　【茨捨て】　　【波動砲(塔踏み)】
　H1 MT H2　 　    D4　　　D3
　D3  ▲   ST　 　 　 　D2 D1
　D1 D4 D2　 　 　 　ST MT
　TH→南西　　　　H2　　　H1
　DPS→北東
ーーーーーーーーーーーーーーーーー
【暗黒天空】　　　　【十字】
　　　　　　　　 　　　D3
　MT D3 D2　　 　　　MT
　H1  ▲  H2　　H1 D1 ▲ D2 H2
　D1  D4 ST　　　　　  ST
　　　　　　　　 　　　D4
ーーーーーーーーーーーーーーーーー
【ヘアカット西】　【ヘアカット東】
　　　　  D3　　　　D3
　　  MT  D2　　 　　H1 MT
　H1 D1  ▲　　  　　 ▲  D2 H2
　　  ST  H2　　 　　D1 ST
　　　　  D4　　 　　D4
```

<details markdown=block>
<summary>Akito's Empty Plane</summary>

To replace Yamipika with Akito's original Empty Plane positions, swap in the following blocks. Note the melee positions in Empty Plane- they will disconnect from the boss when it comes to the 十-formation.

```
【暗黒天空】　　　　【十字】
　　　　　　　　 　　　D3
　H1 D3 MT　　 　　　MT
　D1  ▲  D2　　D1 H1 ▲ H2 D2
　ST  D4 H2　　　　　  ST
　　　　　　　　 　　　D4
ーーーーーーーーーーーーーーーーー
【ヘアカット西】　【ヘアカット東】
　　　　  D3　　　　D3
　　  MT  D2　　 　　H1 MT
　D1 H1  ▲　　  　　 ▲  H2 D2
　　  ST  H2　　 　　D1 ST
　　　　  D4　　 　　D4
```

</details>

## Markers

The markers are used to drop seeds for Brambles.
![](images/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"E9S","MapID":750,"A":{"X":100.0,"Y":0.0,"Z":81.5,"ID":0,"Active":true},"B":{"X":118.5,"Y":0.0,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.0,"Z":118.5,"ID":2,"Active":true},"D":{"X":81.5,"Y":0.0,"Z":100.0,"ID":3,"Active":true},"One":{"X":110.5,"Y":0.0,"Z":89.5,"ID":4,"Active":true},"Two":{"X":110.5,"Y":0.0,"Z":110.5,"ID":5,"Active":true},"Three":{"X":89.5,"Y":0.0,"Z":110.5,"ID":6,"Active":true},"Four":{"X":89.5,"Y":0.0,"Z":89.5,"ID":7,"Active":true}}
```

</details>

## Timeline

![](https://preview.redd.it/ngc2jw12ao661.png?width=3200&format=png&auto=webp&s=e12fc29480f9925ae0f8e4011814345e4a0b2759)
*(Credit: [u/Syldris](https://www.reddit.com/r/ffxiv/comments/kg9oko/e9s_timeline_image/))*