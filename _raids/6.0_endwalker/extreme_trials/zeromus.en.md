---
layout: default
title: Zeromus EX
parent: Extreme Trials
nav_order: 7
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/extreme_trials/zeromus/
---

# The Abyssal Fracture (Extreme)

[Game8.jp](https://game8.jp/ff14/557945) has gone ahead with Hamkatsu's strat:

{% include youtube.html id="jfL35wWxylY" %}

### English

{% include_relative macros/zeromus.en.md %}

### Japanese

{% include_relative macros/zeromus.jp.md %}

## Markers

All markers (except for a center marker) mark safe spots during *Visceral
Whirl*.

In addition, the `AB` markers are for the party to stack at during *Black
Hole*, while the `12` markers are for the marked player dropping the *Black
Hole*.

![]({{site.baseurl}}/images/6.0_endwalker/zeromus/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"Zeromus EX",
  "MapID":965,
  "A":{"X":93.0,"Y":0.0,"Z":81.2,"ID":0,"Active":true},
  "B":{"X":107.0,"Y":0.0,"Z":81.2,"ID":1,"Active":true},
  "C":{"X":0.0,"Y":0.0,"Z":0.0,"ID":2,"Active":false},
  "D":{"X":0.0,"Y":0.0,"Z":0.0,"ID":3,"Active":false},
  "One":{"X":81.2,"Y":0.0,"Z":81.2,"ID":4,"Active":true},
  "Two":{"X":118.8,"Y":0.0,"Z":81.2,"ID":5,"Active":true},
  "Three":{"X":118.8,"Y":0.0,"Z":93.0,"ID":6,"Active":true},
  "Four":{"X":81.2,"Y":0.0,"Z":93.0,"ID":7,"Active":true}
}
```
</details>

## Meteors

The Meteors spawn in one of three possible arrangements.

Here's how you can drop both sets of meteors/tethers, depending on which side
goes first.

![]({{site.baseurl}}/images/6.0_endwalker/zeromus/meteors.jpg)
*(Credit: radrauser)*

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Meteors]</b> Can you jump off the edge to remove a tether?
</summary>
<table>
  <tr>
    <td>
      <p>Alas, no- once the tethers come out, they persist through death.</p>
      <p>You'll respawn at the start point, where the southern meteor is, still
      tethered, and wipe the raid.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Meteors]</b> Can a tank invuln the tethers and not stretch their tether
  instead?
</summary>
<table>
  <tr>
    <td>
      <p>Alas, no- the damage from the tethers ignores invulnerability.</p>
      <p>With some help from the party, an unstretched tether <em>can</em> be
      super-mitigated- it will hit a tank for about 300% of their max HP 
      (remember there are Max HP down debuffs at the time!).</p>
      <p>Unlike other proximity-based damage checks, the tethers do 
      <em>not</em> have a linear falloff, and are instead a binary pass/fail
      check.</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
