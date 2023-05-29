---
layout: default
title: Golbez EX
parent: Extreme Trials
nav_order: 6
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/extreme_trials/golbez/
---

# The Voidcast Dais (Extreme)

There are two strats that are going around:

1. [Game8/Modified Hamkatsu](#game8modified-hamkatsu) *(this is by far the more common strat)*
2. [FFO](#ffo)

### Things to check

Check the following things:

1. How the groups are split for Void Stardust.
  - Game8/Hamkatsu puts the **MT group north, ST group south**.
  - Nukemaru/FFO puts the **MT group west, ST group east**.
2. The stack positions during Terrastorm + Arctic Assault.
  - Game8/Hamkatsu puts the **MT group outside, ST group inside**.
  - Nukemaru/FFO puts the **MT group inside, ST group outside**.
  - The FFO melee uptime variant puts **melee inside** (MTH1D1D2), and **ranged outside** (STH2D3D4).

To summarize:

- **Game8** → N/S Stardust, MT group outside *(most common)*
- **FFO/Nukemaru** → E/W Stardust, MT group inside
- **FFO melee uptime** (アース氷近接内) → E/W Stardust, melee inside

## Game8/Modified Hamkatsu

[Game8](https://game8.jp/ff14/529320) has gone ahead with Hamkatsu's strat for Golbez EX.

{% include youtube.html id="Js6k0I2yImw" %}

*N.B: Hamkatsu has released a [follow-up video](https://youtu.be/uqJI2jL-8rw) where he updated the Gale Sphere positions to melee-in, ranged-out.

The key points to note are:
- Void Stardust splits are **North/South**.
- The MT group is **outside** for Terrastorm + Arctic Assault + stacks.

### English

```
{% include_relative macros/golbez_g8.en.txt %}
```

### Japanese

```
{% include_relative macros/golbez_g8.jp.txt %}
```

## FFO

Nukemaru has also released their guide to the fight. Nukemaru's strat and FFO are very similar with one exception ([see below](#frequently-asked-questions)).

{% include youtube.html id="yuaQqB-Wi60" %}

The key points to note are:
- Void Stardust splits are **East/West**.
- The MT group is **inside** for Terrastorm + Arctic Assault + stacks.

### English

```
{% include_relative macros/golbez_ffo.en.txt %}
```

### Japanese

```
{% include_relative macros/golbez_ffo.jp.txt %}
```

To get the FFO melee uptime variant, the groups for Terrastorm + Arctic Assault + stacks would be:

- Melees in (MTH1D1D2)
- Ranged out (STH2D3D4)

## Markers

Game8/Hamkatsu uses the following markers:

- `ABCD` are for orientation. 
- The `1` marker in the middle is for the healer knockback position.
![](images/markers1.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"Golbez EX","MapID":950,"A":{"X":100.0,"Y":0.029,"Z":87.0,"ID":0,"Active":true},"B":{"X":113.0,"Y":0.029,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.029,"Z":113.0,"ID":2,"Active":true},"D":{"X":87.0,"Y":0.029,"Z":100.0,"ID":3,"Active":true},"One":{"X":100.0,"Y":0.029,"Z":100.0,"ID":4,"Active":true},"Two":{"X":100.0,"Y":0.029,"Z":100.0,"ID":5,"Active":false},"Three":{"X":100.0,"Y":0.029,"Z":100.0,"ID":6,"Active":false},"Four":{"X":100.0,"Y":0.029,"Z":100.0,"ID":7,"Active":false}}
```
</details>

You can use these markers instead:

- `ABCD` are for orientation. 
- The `1234` markers demarcate the boundaries of the Gale Force line AoEs (markers are *not* safe), and players can stand on the markers to get knocked back to the towers.
![](images/markers2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"Golbez EX","MapID":950,"A":{"X":100.0,"Y":0.029,"Z":87.0,"ID":0,"Active":true},"B":{"X":113.0,"Y":0.029,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.029,"Z":113.0,"ID":2,"Active":true},"D":{"X":87.0,"Y":0.029,"Z":100.0,"ID":3,"Active":true}, "One":{"X":103.9,"Y":0.029,"Z":96.1,"ID":5,"Active":true}, "Two":{"X":103.9,"Y":0.029,"Z":103.9,"ID":7,"Active":true}, "Three":{"X":96.1,"Y":0.029,"Z":103.9,"ID":6,"Active":true}, "Four":{"X":96.1,"Y":0.029,"Z":96.1,"ID":4,"Active":true}}
```
</details>

## Frequently Asked Questions

<details markdown=block>
<summary><b>[Nukemaru/FFO]</b> What is the difference between the two?</summary>
<table>
  <tr><td><p>The difference is how the two strategies resolves the 4:4 light party stacks during Gale Sphere #2 and #3.</p>
  <ul>
    <li>The <b>FFO strat</b> follows Hamkatsu, and puts the MT group towards N/W, and the ST group towards S/E.</li>
    <li><b>Nukemaru's strat</b> mirrors the Terrastorm + Arctic Assault stacks, with the MT group near the boss, and the ST group away.</li>
  </ul>
  <p>If you take Nukemaru's strat, and replace Gale Spheres with the (modified) Hamkatsu's method, you get the FFO strat.</p></td></tr>
</table>
</details>