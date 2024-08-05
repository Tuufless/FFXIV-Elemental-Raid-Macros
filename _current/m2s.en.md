---
layout: default
title: M2S
nav_order: 4
permalink: /7.0_dawntrail/savage_raids/m2s/
---

# AAC Light-heavyweight M2 (Savage)

[Game8](https://game8.jp/ff14/630353) has gone along with Nukemaru's strat.

{% include youtube.html id="p9tE-x0XEC4" %}
*(English subtitled)*

### English

```
{% include macros/7.0_dawntrail/m2s.en.txt %}
```

### Japanese

```
{% include macros/7.0_dawntrail/m2s.jp.txt %}
```

## Markers

There are a couple different markers you can use.

### Nukemaru's markers

These are the markers used on Nukemaru's video. You may sometimes see the
`1234` markers rotated such that `1` is on the North-West.

- The `ABCD` markers are just for orientation.
- The `1234` markers mark the boundary for the boss's line AoEs (markers are
  safe).

![]({{site.baseurl}}/images/7.0_dawntrail/m2s/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"M2S (Nukemaru)",
  "MapID":988,
  "A":{"X":100.0,"Y":0.0,"Z":86.0,"ID":0,"Active":true},
  "B":{"X":114.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":114.0,"ID":2,"Active":true},
  "D":{"X":86.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":108.625,"Y":0.0,"Z":91.375,"ID":5,"Active":true},
  "Two":{"X":108.625,"Y":0.0,"Z":108.625,"ID":6,"Active":true},
  "Three":{"X":91.375,"Y":0.0,"Z":108.625,"ID":7,"Active":true},
  "Four":{"X":91.375,"Y":0.0,"Z":91.375,"ID":4,"Active":true}
}
```

</details>

### Box markers

I personally prefer these markers. In addition to the points in the markers
above:

- The `ABCD` markers are in melee range of the boss while still dodging *Honey 
  Beeline* and the point-blank AoE in *Centerstage/Outerstage Combo*.

![]({{site.baseurl}}/images/7.0_dawntrail/m2s/box_markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"M2S (Box)",
  "MapID":988,
  "A":{"X":100.0,"Y":0.0,"Z":91.375,"ID":0,"Active":true},
  "B":{"X":108.625,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":108.625,"ID":2,"Active":true},
  "D":{"X":91.375,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":91.375,"Y":0.0,"Z":91.375,"ID":7,"Active":true},
  "Two":{"X":108.625,"Y":0.0,"Z":91.375,"ID":4,"Active":true},
  "Three":{"X":108.625,"Y":0.0,"Z":108.625,"ID":5,"Active":true},
  "Four":{"X":91.375,"Y":0.0,"Z":108.625,"ID":6,"Active":true}
}
```

</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
