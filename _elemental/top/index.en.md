---
layout: default
title: Lv 90. TOP
nav_order: 5
has_children: true
has_toc: false
permalink: /elemental/top/
---

# The Omega Protocol (Ultimate)

Elemental's TOP PF strat can be broken down as follows:

- [**(Beetle) Omega**](01_omega): HTDH priority, NW/SE Pantokrator
- [**Omega M/F**](02_omega_mf): 1234 (〇×▽□)-4231
- [**(Final) Omega**](03_omega_reconfigured): Astoh monitors
- [**Blue Screen**](04_blue_screen): TRHM, melee adjust
- **Run: Dynamis**
  - [**Delta**](05_run_dynamis_delta): Awk
  - [**Sigma**](05_run_dynamis_sigma): Waymark towers
  - [**Omega**](05_run_dynamis_omega)
- [**Alpha Omega**](06_alpha_omega): Clock spread, Wave Cannon stack east

### BiS Notes

- Any gear at or above **i760** will have their substats capped.
- Relic weapons will have their substats capped at **287**.
- Use the highest available food and potions.

<a href="{{site.baseurl}}/top_cheatsheet.jpg">
  <img src="{{site.baseurl}}/top_cheatsheet.jpg">
</a>
*(Other languages: [日本語]({{site.baseurl}}/top_cheatsheet_jp.jpg), [中文(台灣)]({{site.baseurl}}/top_cheatsheet_zhtw.jpg))*

---

## PoVs

Here are some clear PoVs that I've been collecting.

- [MT PoV (WAR)](https://youtube.com/live/ddu61i9cG6Q)
- [ST PoV (PLD)](https://youtube.com/live/sn_3cjm2vIo)
- [H1 PoV (WHM)](https://youtube.com/live/4OtrT1IDH5c)
- [H2 PoV (SGE)](https://youtube.com/live/wklF6mteicY)
- [D1 PoV (SAM)](https://youtube.com/live/_zxDr1mJLbo)
- [D2 PoV (NIN)](https://youtube.com/live/IWayItot1o8)
- [D3 PoV (BRD)](https://youtube.com/live/r-a6z9Ys4OU)
- [D4 PoV (BLM)](https://youtube.com/live/bB3v9ev093I)

---

## Things to note

- Using automarkers to mark players for the transition to P3, and to mark
  player positions in Delta, Sigma, and Omega is considered the norm (*use at
  your own risk*).

---

## English

{% include_relative macros/top.en.md %}


<details markdown=block>
<summary>日本語</summary>

{% include_relative macros/top.jp.md %}

</details>

---

## Markers

The markers are used for orientation, and several mechanics throughout the
encounter.

- P2: The markers demarcate the boundary for Omega-F's AoE in *Party Synergy*,
  and the Optical Unit's (the giant eye) laser beam.
- P3: The markers act as guidelines for where to stand during *Oversampled Wave
  Cannon*.
- P5a: The marker demarcate the boundary for the Optical Unit's laser beam, and
  where to stand for *Hello, World*.
- P5b: One line in front of the markers demarcate how close you can get for
  *Remote Glitch*, and where the *Hello, World* stand.
- P5c: The markers demarcate the near/middle/far distance needed to dodge
  Omega-M+F's AoEs.
- P6: The markers demarcate the boundary between AoEs during *Cosmo Arrow*, and
  where to run at the start of *Unlimited Wave Cannon*.

![]({{site.baseurl}}/images/ultimates/top/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"TOP",
  "MapID":908,
  "A":{"X":100.0,"Y":0.0,"Z":87.0,"ID":0,"Active":true},
  "B":{"X":113.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":113.0,"ID":2,"Active":true},
  "D":{"X":87.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":109.192,"Y":0.0,"Z":90.808,"ID":4,"Active":true},
  "Two":{"X":109.192,"Y":0.0,"Z":109.192,"ID":5,"Active":true},
  "Three":{"X":90.808,"Y":0.0,"Z":109.192,"ID":6,"Active":true},
  "Four":{"X":90.808,"Y":0.0,"Z":90.808,"ID":7,"Active":true}
}
```

</details>

---

## Frequently Asked Questions

<details markdown=block>
<summary>
  <b>[Damage Down]</b> How strong is the damage down debuff in this fight?
</summary>
<table>
  <tr>
    <td>
      <p>The Damage Down debuff in this phase lowers a player's damage by
      <b>90%</b>.</p>
      <p><em>(Yes, this is </em>worse<em> than double-weakness!)</em></p>
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>