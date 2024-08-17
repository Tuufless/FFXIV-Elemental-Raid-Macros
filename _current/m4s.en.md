---
layout: default
title: M4S
nav_order: 6
permalink: /7.0_dawntrail/savage_raids/m4s/
---

# AAC Light-heavyweight M4 (Savage)

Game8 has gone along with Nukemaru's strat. Explanation has been split into two 
parts, even though this is a single encounter with no checkpoint.

- [Part 1](https://game8.jp/ff14/631136)
- [Part 2](https://game8.jp/ff14/631340)

Nukemaru has also split his guide into two parts:

**First half:**

{% include youtube.html id="gl4BNKLr3rk" %}
*(English subtitled)*

**Second half:**

{% include youtube.html id="vFh4YWxUVrE" %}
*(English subtitled)*

### English

```
{% include macros/7.0_dawntrail/m4s.en.txt %}
```

### Japanese

```
{% include macros/7.0_dawntrail/m4s.jp.txt %}
```

## Markers

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

## Timeline
![](https://lh3.googleusercontent.com/pw/AP1GczMMyMo9Hu-zy6LIGLIcCDQ7SqWm9KujuglARA55OdUtLhSDa-r0lS2922ytKh-PUJjAwppNHl9shYUM--MwBrVM-22caQyar96-4-RqQvzLjW-YFYk9ll1-uz-k3vM-DtC61i3LmNsbuffy5rcdOkWJ=w1079-h911-s-no-gm?authuser=0)
*([Full size image](https://lh3.googleusercontent.com/pw/AP1GczMMyMo9Hu-zy6LIGLIcCDQ7SqWm9KujuglARA55OdUtLhSDa-r0lS2922ytKh-PUJjAwppNHl9shYUM--MwBrVM-22caQyar96-4-RqQvzLjW-YFYk9ll1-uz-k3vM-DtC61i3LmNsbuffy5rcdOkWJ=w1079-h911-s-no-gm?authuser=0), Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/1eigxar/m4s_timeline_spoiler_70/))*

### Team DN's Witch Hunt

This was a [strat used by Team DN](https://twitter.com/Lial_Varia/status/1818672413585928380)
that simplifies things by allowing **players to ignore whether the baited dives 
will go on the near, or far players**.

Note that the markers used in the diagrams before are the markers that are 
being populated by JP PF, and are *not* the markers that the group originally 
used.

<table>
  <tr>
    <td width="50%">
      <p>Each role has two reference points that dodge the boss's <em>Narrowing 
      Witch Hunt</em> or <em>Widening Witch Hunt</em>.</p>
      <p>Then, each reference point has <b>two</b> positions- one "inner" and
      one "outer" position.</p>
      <p>Using the diagram to the right, all players will dodge to the <b>green
      → green → red → red</b> marks, based on their clock positions.</p>
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/witch_hunt.jpg">
    </td>
  </tr>
</table>

The reference points and positions are very specific:

<table>
  <tr>
    <td></td>
    <td style="text-align:center" width="40%">
      <b>Inside reference point</b>
    </td>
    <td style="text-align:center" width="40%">
      <b>Outside reference point</b>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <b>Tanks + Melee</b>
    </td>
    <td>
      <p>Use the boss's targeting circle.</p>
      <ul>
        <li><b>Inner:</b> Just inside the targeting circle.</li>
        <li><b>Outer:</b> Just outside the targeting circle.</li>
      </ul>
    </td>
    <td>
      <p>Use the cardinal waymark.</p>
      <ul>
        <li><b>Inner:</b> On the outer half of the marker.</li>
        <li><b>Outer:</b> Just past the marker.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <b>Healers + Ranged</b>
    </td>
    <td>
      <p>Use the intercardinal waymark.</p>
      <ul>
        <li><b>Inner:</b> On the outer corner of the waymark.</li>
        <li><b>Outer:</b> Just past the outer corner of the waymark.</li>
      </ul>
    </td>
    <td>
      <p>Use the junction where four tiles meet.</p>
      <ul>
        <li><b>Inner:</b> Just before the junction.</li>
        <li><b>Outer:</b> On the junction, or further.</li>
      </ul>
    </td>
  </tr>
</table>

Once you have established the two anchor points, your dodges will go:

- **Tanks + Ranged:** Inner → Inner → Outer → Outer
- **Healers + Melee:** Outer → Outer → Inner → Inner

Put together, it will look like this:

<table>
  <tr>
    <td colspan="2">
      <p><b>1st and 2nd <em>Witch Hunts</em>:</b></p>
      <ul>
        <li><b>Tanks + Ranged:</b> Inner positions.</li>
        <li><b>Healers + Melee:</b> Outer positions.</li>
      </ul>
      <p>The tanks will take the near-dives, while the healers will take the
      far-dives.</p>
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
      <p><b>3rd and 4th <em>Witch Hunts</em>:</b></p>
      <ul>
        <li><b>Tanks + Ranged:</b> Outer positions.</li>
        <li><b>Healers + Melee:</b> Inner positions.</li>
      </ul>
      <p>The melee will take the near-dives, while the ranged will take the
      far-dives.</p>
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

### Kuuya's Electron Stream

[Kuuya's Electron Stream](https://twitter.com/kuuya_ava/status/1818663317055082797)
is a method to resolve all the debuffs in *Electron Stream* that minimises
movement and maintains melee uptime.

It is essentially identical to Team DN's solution, *however*, Kuuya has tanks
and healers drop their AoEs/donuts *towards the wall*, while DPS drop theirs
*towards the inside* of the arena.

<table>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/roundhouse_conductor.png">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/spinning_conductor.png">
    </td>
    <td>
      <p><em>Roundhouse Conductor/Spinning Conductor</em></p>
      <p>Stand on the "rivet" towards the corner of the tile, towards the
      boss.</p>
      <ul>
        <li><b>Tanks/Healers</b>: Towards the outside (the wall).</li>
        <li><b>DPS</b>: Towards the inside (where the floor used to be).</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/proximate_current.png">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/remote_current.png">
    </td>
    <td>
      <p><em>Proximate Current/Remote Current</em></p>
      <p>Stand just in front of the center of the tile (in front of the player
      with <em>Collider Conductor</em>).</p></td>
  </tr>
  <tr>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/collider_conductor.png">
    </td>
    <td>
      <p><em>Collider Conductor</em></p>
      <p>Stand just behind the center of the tile (behind the player with
      <em>Proximate/Remote Current</em>).</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" style="text-align:center">
      <img src="{{site.baseurl}}/images/7.0_dawntrail/m4s/ion_cluster.jpg">
    </td>
  </tr>
</table>

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Electron Stream]</b> Why do the players go to the outside/inside instead
  of to the left/right?
</summary>
<table>
  <tr>
    <td>
      <p>At least two groups independently came up with essentially the same
      solution, with the only difference being where the <em>Conductor</em>
      debuffs go.</p>
      <ul>
        <li><b>One Ace</b> is the Japanese group that Kuuya was part of, and
        put tanks/healers to the wall, and DPS on the inside.</li>
        <li><b>Team DN</b> is the NA group that got World 6th, and put
        tanks/healers to the left (facing the boss), and DPS to the right.</li>
      </ul>
      <p>Which scheme you choose is ultimately an arbitrary decision.</p>
      <p>One Ace, being a Japanese group, has more influence over the Japanese
      player base, hence why tanks/healers go to the wall in the Japanese
      DCs.</p>
    </td>
  </tr>
</table>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
