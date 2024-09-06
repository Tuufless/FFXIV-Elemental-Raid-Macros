---
layout: default
title: Golbez EX
parent: Extreme Trials
nav_order: 6
grand_parent: 6.0 Endwalker
permalink: /6.0_endwalker/extreme_trials/golbez/
---

# The Voidcast Dais (Extreme)

[Game8.jp](https://game8.jp/ff14/529320) has gone ahead with a modified version of
Hamkatsu's strat for Golbez EX.

{% include youtube.html id="Js6k0I2yImw" %}

*N.B: Hamkatsu has released a [follow-up video](https://youtu.be/uqJI2jL-8rw)
where he updated the Gale Sphere positions to melee-in, ranged-out.

The key points to note are:
- Void Stardust splits are **North/South**.
- The MT group is **outside** for Terrastorm + Arctic Assault + stacks.

### English

{% include_relative macros/golbez.en.md %}

### Japanese

{% include_relative macros/golbez.jp.md %}

## Markers

Game8/Hamkatsu uses the following markers:

- `ABCD` are for orientation. 
- The `1` marker in the middle is for the healer knockback position.
![]({{site.baseurl}}/images/6.0_endwalker/golbez/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"Golbez EX",
  "MapID":950,
  "A":{"X":100.0,"Y":0.029,"Z":87.0,"ID":0,"Active":true},
  "B":{"X":113.0,"Y":0.029,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.029,"Z":113.0,"ID":2,"Active":true},
  "D":{"X":87.0,"Y":0.029,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":100.0,"Y":0.029,"Z":100.0,"ID":4,"Active":true},
  "Two":{"X":100.0,"Y":0.029,"Z":100.0,"ID":5,"Active":false},
  "Three":{"X":100.0,"Y":0.029,"Z":100.0,"ID":6,"Active":false},
  "Four":{"X":100.0,"Y":0.029,"Z":100.0,"ID":7,"Active":false}
}
```
</details>

## Timeline
![](https://preview.redd.it/ap6oimoekt1b1.png?width=2177&format=png&auto=webp&v=enabled&s=89dc7a5fd1b07d415e23b1c263c361b56ce46d29)
*(Credit: [u/ExiaKuromonji](https://www.reddit.com/r/ffxiv/comments/13qswiz/spoiler_64_ex6_abilities_and_timeline/))*

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Game8]</b> What was the modification made to Hamkatsu's to get to Game8's
  strat?
</summary>
<table>
  <tr>
    <td>
      <p>The difference is in the lineup for Gale Spheres #2 and #3.</p>
      <p>Hamkatsu's original strategy has the tanks/healers and DPS line up
      differently:</p>
      <ul>
        <li><b>N/W：</b> MTD1 > STD2 > H1D3 > H2D4 <b>：S/E</b></li>
      </ul>
      <p>This has a couple issues, namely that it is difficult for the MT and
      D1 to maintain uptime on the boss.</p>
      <p>Hamkatsu released a <a href="https://youtu.be/uqJI2jL-8rw/">follow-up video</a>
      where he updated the Gale Sphere positions to what we have now (melee-in,
      ranged-out), which Game8 picked up, hence the "Modified Hamkatsu".</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Void Stardust]</b> Why are the groups split N/S instead of E/W?
</summary>
<table>
  <tr>
    <td>
      <p>This was one of the points of contention when the fight was released.
      Unfortunately, we don't know why Hamkatsu split the groups N/S,
      especially when Eventide Fall means H1 may have to cross from NE to W,
      and H2 from SW to E.</p>
    </td>
  </tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Terrastorm + Arctic Assault]</b> Why does the MT group go outside and the
  ST group stay in?
</summary>
<table>
  <tr>
    <td>
      <p>This was one of the points of contention when the fight was released.
      We don't know why Hamkatsu put the MT group on the outside, but this was
      what PF eventually settled to.</p>
      <p>Many players felt that having the MT group stay towards the center,
      and the ST group go out made more sense. Another configuration had all
      the melees inside together with H1, and the ranged (with the ST)
      outside.</p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
