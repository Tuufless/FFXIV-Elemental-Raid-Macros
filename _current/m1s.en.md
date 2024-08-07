---
layout: default
title: M1S
nav_order: 3
permalink: /7.0_dawntrail/savage_raids/m1s/
---

# AAC Light-heavyweight M1 (Savage)

[Game8](https://game8.jp/ff14/630292) has gone with Inumaru's strat for M1S as
a base, changing:

- The knockback/knockup *Elevate and Eviscerate* mechanic. Game8 is going with
  the single-tile strat.
  - When marked, that player goes to their tile and positions themselves to get 
    knocked from one corner diagonally to the other corner of the the same
    tile, thus ignoring which stance the clone is actually in.
  - Melees take the two inner tiles, while ranged take the two outer tiles,
    with the boss staying in the center.

{% include youtube.html id="S1SBXo9tLfo" %}

### English

```
{% include macros/7.0_dawntrail/m1s.en.txt %}
```

### Japanese

```
{% include macros/7.0_dawntrail/m1s.jp.txt %}
```

## Markers

- The `ABCD` markers are for orientation.
- The `1234` markers are where the clones will teleport to for *Nine Lives* #2.

![]({{site.baseurl}}/images/7.0_dawntrail/m1s/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"M1S",
  "MapID":986,
  "A":{"X":100.0,"Y":0.0,"Z":90.0,"ID":0,"Active":true},
  "B":{"X":110.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":110.0,"ID":2,"Active":true},
  "D":{"X":90.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":110.0,"Y":0.0,"Z":95.0,"ID":4,"Active":true},
  "Two":{"X":110.0,"Y":0.0,"Z":105.0,"ID":5,"Active":true},
  "Three":{"X":90.0,"Y":0.0,"Z":105.0,"ID":6,"Active":true},
  "Four":{"X":90.0,"Y":0.0,"Z":95.0,"ID":7,"Active":true}
}
```

</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
