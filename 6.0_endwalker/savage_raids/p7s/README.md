---
layout: default
title: P7S
parent: Savage Raids
nav_order: "07"
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/savage_raids/p7s/
---

# Abyssos: The Seventh Circle (Savage)

PF uses [Shinosho's strat](https://youtu.be/JOMBTuWf-j8) as a base, but modifies the following sections:

- [Sleepo's strat for Inviolate Purgation](https://ff14.toolboxgaming.space/?id=339073562612661&preview=1).
- Fixed positions strat for Death's Harvest.
- Inumaru's strat for War's Harvest.

### Things to check on Party Finder

- Check the Purgation positions, **especially if you join a Japanese party**.

## English
*(I expect this to change when Game8 releases their macro)*
```
【Forbidden Fruit 1】
　Near：MTH1D1D3　Far：STH2D2D4
【Inviolate Bonds】
　MT/D1　ST/D2
　H1/D3　H2/D4
【Forbidden Fruit 2 (Shinosho)】
　　 　D1　　　D2
　D3　・ MT　ST ・　D4　　※ Healers use
 　　　　　  ▼ 　　　　　　　 　anti-kb
 　　　 H1　・　  H2
【Forbidden Fruit 3 / Knockback→stacks】
　West：MTH1D1D3　East：STH2D2D4
【Forbidden Fruit 5】
　Point birds away from close birds + 
　anti-knockback
【Inviolate Purgation (Sleepo)】
　　　　MT/D1　　　MT/D1　　※ Starting point
　(stack)　　　　　　　　　　(stack)　　NW>NE
　　　　H1/D2（bird）H1/D2
　ST/D3　　　　　　　　　　ST/D3
　　　　H2/D4　　　H2/D4
　Light of Life #1：MT Reprisal, MT 90s, D3
　Light of Life #2：ST Reprisal, ST 90s, D4
【Death's Harvest (Fixed pos, tank invuln)】
 　　　　　★　　　　　　※ Use add on platform
　　　　／／＼＼　　　　　　as North
　　　H1 　　　H2　　　※ MTST stack on empty
　D3　　　　　　　D4　　　bridge + invuln
　　　　D1 　D2
【War's Harvest  (inumaru)】
　※20% mit or 10% mit + shields
　      ☆   ☆　　　B Tether
　 ☆   C     M →→ B →→ M Tether
 　   ☆　　　      M
　　　       　     /
   　                B
　　　　    /　  B Tether
　　　M Tether
　※C = cow, B = bird, M = mino
```

## Markers (placeable in-game)

These are the markers I use, and can be placed in-game.

- `123`: Center of the three platforms when the arena changes.

In particular, I use square markers because the flat edges give a reference to where True North is to help players align themselves for Purgation.

![](images/markers_placeable.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"P7S","MapID":877,"A":{"X":0.0,"Y":0.0,"Z":0.0,"ID":0,"Active":false},"B":{"X":0.0,"Y":0.0,"Z":0.0,"ID":1,"Active":false},"C":{"X":0.0,"Y":0.0,"Z":0.0,"ID":2,"Active":false},"D":{"X":0.0,"Y":0.0,"Z":0.0,"ID":3,"Active":false},"One":{"X":85.7106,"Y":0.0,"Z":91.75,"ID":4,"Active":true},"Two":{"X":114.2894,"Y":0.0,"Z":91.75,"ID":5,"Active":true},"Three":{"X":100.0,"Y":0.0,"Z":116.5,"ID":6,"Active":true},"Four":{"X":100.0,"Y":0.0,"Z":100.0,"ID":7,"Active":true}}
```

</details>

## Markers (Sleepo - not placeable in-game)

These set of markers **must** be placed via the XIVLauncher WaymarkPresetPlugin.

If you don't have the plugin (or play on console), you will need to copy the markers from someone who does.

All markers are used for Sleepo's Purgation.

- `2` and `B`: Stack positions.
- All other markers are the spread positions.

![](images/markers_sleepo.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"P7S (Sleepo)","MapID":877,"A":{"X":114.29,"Y":0.0,"Z":82.75,"ID":0,"Active":true},"B":{"X":122.084,"Y":0.0,"Z":87.25,"ID":1,"Active":true},"C":{"X":122.0842,"Y":0.0,"Z":96.25,"ID":2,"Active":true},"D":{"X":114.29,"Y":0.0,"Z":100.75,"ID":3,"Active":true},"One":{"X":85.71,"Y":0.0,"Z":82.75,"ID":4,"Active":true},"Two":{"X":77.915,"Y":0.0,"Z":87.25,"ID":5,"Active":true},"Three":{"X":77.915,"Y":0.0,"Z":96.25,"ID":6,"Active":true},"Four":{"X":85.71,"Y":0.0,"Z":100.75,"ID":7,"Active":true}}
```

</details>