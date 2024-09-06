---
layout: default
title: Barbariccia EX
parent: Extreme Trials
nav_order: 4
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/extreme_trials/barbariccia/
---

# Storm's Crown (Extreme)

This is [Game8.jp's macro](https://game8.jp/ff14/477950).

It's basically [Hamkatsu's strat](https://youtu.be/FToWDK7uy4w), but resolves
Playstation symbols in a "braindead" manner (T/H go to assigned cardinals, DPS
all stack in the center and get pulled to their assigned partner). 

## English

{% include_relative macros/barbariccia.en.md %}

## Japanese

{% include_relative macros/barbariccia.jp.md %}

## Markers

You might see the `ABCD` markers placed further out towards the edge of the arena.

- `ABCD`: Orientation, T/H Playstation positions
- `C`: Party stack during 2x Flares + stack
- `1` and `3`: Enumeration pairs during Teasing Tangles

![]({{site.baseurl}}/images/6.0_endwalker/barbariccia/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"Barbariccia EX",
  "MapID":871,
  "A":{"X":100.0,"Y":0.0,"Z":91.5,"ID":0,"Active":true},
  "B":{"X":108.5,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":108.5,"ID":2,"Active":true},
  "D":{"X":91.5,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":106.0,"Y":0.0,"Z":94.0,"ID":4,"Active":true},
  "Two":{"X":106.0,"Y":0.0,"Z":94.0,"ID":5,"Active":false},
  "Three":{"X":94.0,"Y":0.0,"Z":106.0,"ID":6,"Active":true},
  "Four":{"X":94.0,"Y":0.0,"Z":106.0,"ID":7,"Active":false}
}
```
</details>

## Playstation 2 + Air Bumps

<table>
  <tr>
    <td>
      <p><b>Case 1: Enumeration pairs are opposite each other.</b></p>
      <p>Pair with the player beside you in the adjacent pair.</p>
    </td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/barbariccia/airbumps_1_1.jpg"></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/barbariccia/airbumps_1_2.jpg"></td>
  </tr>
  <tr>
    <td>
      <p><b>Case 2: Enumeration pairs are adjacent to each other.</b></p>
      <p>Stack with the adjacent pair (Enumeration pair + no enumeration pair).</p>
    </td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/barbariccia/airbumps_2_1.jpg"></td>
    <td><img src="{{site.baseurl}}/images/6.0_endwalker/barbariccia/airbumps_2_2.jpg"></td>
  </tr>
</table>

*(Credit: [Game8.jp](https://game8.jp/ff14/477950))*

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
