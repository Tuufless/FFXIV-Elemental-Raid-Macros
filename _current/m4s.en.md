---
layout: default
title: M4S
nav_order: 6
permalink: /7.0_dawntrail/savage_raids/m4s/
---

# AAC Light-heavyweight M4 (Savage)

[Game8](https://game8.jp/ff14/631136) has gone along with [Idyllshire's strat](http://kanatan.info/archives/37662658.html),
using Kuuya's *Ion Cluster*, Mochibe's *Midnight Sabath*, and Ice's *Sunrise 
Sabath* positions.

Idyllshire does not make video guides, but Nukemaru has been iterating on their 
guides to match what PF has been doing, although note that there are still a 
couple differences remaining.

**First half:**

{% include youtube.html id="gl4BNKLr3rk" %}

**Second half:**

{% include youtube.html id="vFh4YWxUVrE" %}

### Japanese

```
{% include macros/7.0_dawntrail/m4s.jp.txt %}
```

## Markers

Nukemaru's markers are pretty common.

- The markers are used for *Narrowing/Widening Witch Hunt*.
- The `A` marker is also used to reference North for the pair/spread positions 
  during *Electrope 1*.

![]({{site.baseurl}}/images/7.0_dawntrail/m4s/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"M4S (Nukemaru)",
  "MapID":992,
  "A":{"X":100.0,"Y":0.0,"Z":90.0,"ID":0,"Active":true},
  "B":{"X":110.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":110.0,"ID":2,"Active":true},
  "D":{"X":90.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":105.0,"Y":0.0,"Z":95.0,"ID":4,"Active":true},
  "Two":{"X":105.0,"Y":0.0,"Z":105.0,"ID":5,"Active":true},
  "Three":{"X":95.0,"Y":0.0,"Z":105.0,"ID":6,"Active":true},
  "Four":{"X":95.0,"Y":0.0,"Z":95.0,"ID":7,"Active":true}
}
```

</details>

## DN's Witch Hunt

This was a [strat used by Team DN](https://twitter.com/Lial_Varia/status/1818672413585928380)
that simplifies things by allowing **players to ignore whether the baited dives 
will go on the near, or far players**.

Note that the markers used in the diagrams before are the markers that are 
being populated by JP PF, and are *not* the markers that the group originally 
used.

<table>
  <tr>
    <td width="50%">
      <p>Each role has two anchor points that dodge the boss's <em>Narrowing 
      Witch Hunt</em> or <em>Widening Witch Hunt</em>.</p>
      <p>Then, each anchor point has <b>two</b> positions- one "inner" and one 
      "outer" position.</p>
      <p>Using the diagram to the right, all players will dodge to the <b>green → 
      green → red → red</b> marks, based on their clock positions.</p>
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/witch_hunt.jpg">
    </td>
  </tr>
</table>

In order words, once you have established the two anchor points, your dodges will go:

- **Tanks + Ranged:** Inner → Inner → Outer → Outer
- **Healers + Melee:** Outer → Outer → Inner → Inner

<table>
  <tr>
    <td colspan="2">
      <p><b>1st and 2nd dives:</b></p>
      <ul>
        <li><b>Tanks + Ranged:</b> Inner positions.</li>
        <li><b>Healers + Melee:</b> Outer positions.</li>
      </ul>
      <p>The tanks will take the near-dives, while the healers will take the far-dives.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/witch_hunt_01.jpg">
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/witch_hunt_02.jpg">
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <p><b>3rd and 4th dives:</b></p>
      <ul>
        <li><b>Tanks + Ranged:</b> Outer positions.</li>
        <li><b>Healers + Melee:</b> Inner positions.</li>
      </ul>
      <p>The melee will take the near-dives, while the ranged will take the far-dives.</p>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/witch_hunt_03.jpg">
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/witch_hunt_04.jpg">
    </td>
  </tr>
</table>

### Kuuya's Ion Cluster

Notably, tanks and healers drop their AoEs/donuts *towards the wall*, while DPS 
drop theirs *towards the inside* of the arena.

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">4層前半エレクトロンストリーム位置固定法<br>野良でやりたいから流行ってほしい <a href="https://t.co/jNuSAxUeM5">pic.twitter.com/jNuSAxUeM5</a></p>&mdash; くうや (@kuuya_ava) <a href="https://twitter.com/kuuya_ava/status/1818663317055082797?ref_src=twsrc%5Etfw">July 31, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
