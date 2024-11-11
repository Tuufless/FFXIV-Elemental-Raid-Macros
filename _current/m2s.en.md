---
layout: default
title: M2S
nav_order: 6
permalink: /7.0_dawntrail/savage_raids/m2s/
---

# AAC Light-heavyweight M2 (Savage)

[Game8.jp](https://game8.jp/ff14/630353) has gone along with Nukemaru's strat.

{% include youtube.html id="p9tE-x0XEC4" %}
*(English subtitled)*

---

### English

{% include_relative macros/m2s.en.md %}

### Japanese

{% include_relative macros/m2s.jp.md %}

---

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

---

## Timeline
![](https://lh3.googleusercontent.com/pw/AP1GczNSVhF923-PC6d6QG6M3Fu87Yi5KG2Az-cEBC-Tu0wYEM-kimRgpEAJ_I1J5P4c8c1t5bYN1tU-b7uam0FoPHQo9DWE7sDNnIJeLhiMOY2fe0Qr8PlGkgozMbxNNZh5hxaAPqD8NFdx-NnB-yvggSLE=w1745-h715-s-no-gm?authuser=0)
*([Full size image](https://lh3.googleusercontent.com/pw/AP1GczNSVhF923-PC6d6QG6M3Fu87Yi5KG2Az-cEBC-Tu0wYEM-kimRgpEAJ_I1J5P4c8c1t5bYN1tU-b7uam0FoPHQo9DWE7sDNnIJeLhiMOY2fe0Qr8PlGkgozMbxNNZh5hxaAPqD8NFdx-NnB-yvggSLE=w1745-h715-s-no-gm?authuser=0), Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/1eh1qr3/m2s_timeline_spoiler_70/))*

---

## Frequently Asked Questions

<details markdown=block>
<summary><b>[Damage Down]</b> How strong is the damage down debuff in this 
fight?</summary>
<table>
  <tr>
    <td>
      <p>The Damage Down debuff in this encounter lowers a player's damage by 
      <b>26%</b> for 30 seconds.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Honey B. Live: 1st Beat]</b> Is a ranged player supposed to end up with
  two hearts?
</summary>
<table>
  <tr>
    <td>
      <p>Yes- assuming nobody takes an extra heart, there should be five
      players with two hearts, not four. The party actually has a one-heart
      margin of error.</p>
      <p>If you look closely, that's also why there's a subtle difference
      between the English and Japanese macros:</p>
      <ul>
        <li>The Japanese macro says "all melee get two hearts, and stack
        together."</li>
        <li>The English macro says "all melee get two hearts, then all players
        with two hearts stack together."</li>
      </ul>
      <p>This is important, because the stack targets a random player with the
      fewest hearts (which could be a ranged), but it's also good practice to
      associate "stacking together" with "having two hearts", instead of "being
      melee".</p>
      <p>That means if anyone accidentally messes up and takes one extra heart,
      everything still works out because the remaining four players with two
      hearts can share the stack.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Heartsick (stacks)]</b> How are hearts distributed?
</summary>
<table>
  <tr>
    <td>
      <p>All stacks distribute a total of 4 hearts to players in the stack. Who
      gets the hearts seem to be decided by:</p>
      <ol>
        <li>Pick a maximum of four players at random in the stack (pick
        everybody if the stack has less than 5 players).</li>
        <li>Sort these players from lowest to highest number of hearts.</li>
        <li>Give a heart to those players in that order (looping if needed)
        until there are no more hearts left to distribute.</li>
      </ol>
      <p>As a result:</p>
      <ul>
        <li>If there is only one player in the stack, that player gets four
        hearts.</li>
        <li>If there are two players in the stack, each get two hearts.</li>
        <li>If there are three players in the stack, each get a heart, and
        the extra heart goes to one of the players with the fewest hearts.</li>
        <li>If there are four players in the stack, each gets a heart.</li>
        <li>If there are five or more players in the stack, four of them at
        random get a heart.</li>
      </ul>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Rotten Heart]</b> What's the latest you can trigger the debuffs before
  the raid-wide?
</summary>
<table>
  <tr>
    <td>
      <p>The latest you can trigger the α and β debuffs and have the <em>Magic
      Vulnerability Up</em> wear off before <em>Call Me Honey</em> is when
      there is <b>3 seconds left</b> on the debuff.</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
 