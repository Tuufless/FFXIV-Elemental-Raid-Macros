---
layout: default
title: Golbez EX
parent: Extreme Trials
nav_order: 6
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/extreme_trials/golbez/
---

# The Voidcast Dais (Extreme)

[Game8](https://game8.jp/ff14/529320) has gone ahead with Hamkatsu's strat for Golbez EX.

However, the strat is still very much in turmoil, and has not settled set.

{% include youtube.html id="Js6k0I2yImw" %}

*N.B: Hamkatsu has released a [follow-up video](https://youtu.be/uqJI2jL-8rw) where he updated the Gale Sphere positions to melee-in, ranged-out.

### Things to check

- Check the stack positions for the Meteor + Ice + stacks.
  - The macro says MT group outside, ST group inside.
  - MTH1D1D2 (melee) inside, STH2D3D4 (ranged) outside is also very popular.
- Check how the groups are split for Void Stardust.
  - The macro splits the arena N/S.
  - However, E/W is technically better, especially if healer stacks are fixed to E/W.

## English

```
{% include_relative macros/golbez.en.txt %}
```

## Japanese

```
{% include_relative macros/golbez.jp.txt %}
```

## Markers

Game8/Hamkatsu uses the following markers:

- `ABCD` are for orientation. 
- The `1` marker in the middle is for the healer knockback position.
![](images/markers2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"Golbez EX","MapID":950,"A":{"X":100.0,"Y":0.029,"Z":87.0,"ID":0,"Active":true},"B":{"X":113.0,"Y":0.029,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.029,"Z":113.0,"ID":2,"Active":true},"D":{"X":87.0,"Y":0.029,"Z":100.0,"ID":3,"Active":true},"One":{"X":100.0,"Y":0.029,"Z":100.0,"ID":4,"Active":true},"Two":{"X":100.0,"Y":0.029,"Z":100.0,"ID":5,"Active":false},"Three":{"X":100.0,"Y":0.029,"Z":100.0,"ID":6,"Active":false},"Four":{"X":100.0,"Y":0.029,"Z":100.0,"ID":7,"Active":false}}
```
</details>

I personally quite like these markers:

- `ABCD` are for orientation. 
- The `1234` markers demarcate the boundaries of the Gale Force line AoEs (markers are *not* safe), and players can stand on the markers to get knocked back to the towers.
![](images/markers1.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"Golbez EX","MapID":950,"A":{"X":100.0,"Y":0.029,"Z":87.0,"ID":0,"Active":true},"B":{"X":113.0,"Y":0.029,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.029,"Z":113.0,"ID":2,"Active":true},"D":{"X":87.0,"Y":0.029,"Z":100.0,"ID":3,"Active":true},"One":{"X":96.1,"Y":0.029,"Z":96.1,"ID":4,"Active":true},"Two":{"X":103.9,"Y":0.029,"Z":96.1,"ID":5,"Active":true},"Three":{"X":96.1,"Y":0.029,"Z":103.9,"ID":6,"Active":true},"Four":{"X":103.9,"Y":0.029,"Z":103.9,"ID":7,"Active":true}}
```
</details>