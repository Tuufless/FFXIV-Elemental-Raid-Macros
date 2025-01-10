---
layout: default
title: Lv 100. FRU
nav_order: 6
has_children: true
has_toc: false
permalink: /ultimates/fru/
---

# Futures Rewritten (Ultimate)

My FRU strat is currently a **work in progress**.

<div style="padding: 10px; border: 1px solid;">
<ul>
  <li><b>Current version: v4.0.0</b>
    <ul>
      <li>Fatebreaker: v2.0.0</li>
      <li>Usurper of Frost: v3.3.0</li>
      <li>Oracle of Darkness: v1.1.0</li>
      <li>Gaia and Shiva: v1.0</li>
      <li>Pandora: v1.0</li>
    </ul>
  </li>
</ul>
</div>

I'm using software's semantic versioning ("major.minor.patch") to help keep 
track of changes while things are in flux:

- Major versions change when a significant, or backwards-incompatible change is 
  made (e.g: changing strats).
- Minor versions change when the basic strategy is kept intact, but positions 
  have changed.
- Patch versions change when something minor is tweaked, like moving mitigation
  around.

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
<ul>
  <li><b>Getting a final strategy together will be a time-intensive process, 
  and likely won't settle until the end of Patch 7.1 (roughly March/April
  2025).</b></li>
</ul>
</div>

### BiS Notes

- Use your **i730** BiS.
- Use the highest grade potions available.

Looking towards the future:

- Futures Rewritten will not be outgeared until **i860** gear is available in
Patch 8.0.
- Relic weapons (when they arrive) will have their substats capped at **393**.

![]({{site.baseurl}}/fru_cheatsheet.jpg)
*(Full-size image: [English]({{site.baseurl}}/fru_cheatsheet.jpg))*

## Markers

A number of mechanics are resolved using "coloured marker pairs".

- `A1`: MT + D3, `B2`: ST + D4, `C3`: H2 + D2, `D4`: H1 + D1

Furthermore, when the party needs to split into groups of four:

- `A1D4`: Tanks + healers *or* MT-group, `B2C3`: DPS _or_ ST-group.


![]({{site.baseurl}}/images/ultimates/fru/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"FRU",
  "MapID":1006,
  "A":{"X":100.0,"Y":0.0,"Z":90.0,"ID":0,"Active":true},
  "B":{"X":110.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":110.0,"ID":2,"Active":true},
  "D":{"X":90.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":92.929,"Y":0.0,"Z":92.929,"ID":4,"Active":true},
  "Two":{"X":107.071,"Y":0.0,"Z":92.929,"ID":5,"Active":true},
  "Three":{"X":107.071,"Y":0.0,"Z":107.071,"ID":6,"Active":true},
  "Four":{"X":92.929,"Y":0.0,"Z":107.071,"ID":7,"Active":true}
}
```

</details>

I am also testing these markers out.

The idea behind these markers is to use the `A`/`C` and the `1234` markers to
stack on during *Crystallize Time* with sufficient gap for the tanks to slot in
between.

![]({{site.baseurl}}/images/ultimates/fru/markers2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"FRU (alternating)",
  "MapID":1006,
  "A":{"X":100.0,"Y":0.0,"Z":88.6,"ID":0,"Active":true},
  "B":{"X":111.4,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":111.4,"ID":2,"Active":true},
  "D":{"X":88.6,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":93.8,"Y":0.0,"Z":93.8,"ID":4,"Active":true},
  "Two":{"X":106.2,"Y":0.0,"Z":93.8,"ID":5,"Active":true},
  "Three":{"X":106.2,"Y":0.0,"Z":106.2,"ID":6,"Active":true},
  "Four":{"X":93.8,"Y":0.0,"Z":106.2,"ID":7,"Active":true}
}
```

</details>

---

## Frequently Asked Questions

<details markdown=block>
<summary><b>[Markers]</b> Is there a particular reason the 1 marker is NW 
instead of NE?</summary>
<table>
  <tr><td><p>Yes. Because melee want rear positionals, putting D1 and D2 at 
  the boss's rear leads to the "MT group west, ST group east" split, or 
  more specifically, everything from N to SW being the "MT group's" half.</p>
  <p>The only way to get that and still give melee rear positionals is to split
   the arena between the West and East.</p>
   <p>In FRU's case, many mechanics can be resolved based on either "ranged + 
  melee" pairs (e.g: the crystals phase) or "tank/healer + DPS" pairs (e.g: 
  <em>Cyclonic Break</em>), which leads to being able to assign mechanics 
  based on coloured quadrants (e.g: the MT+D3 pair is responsible for the "red 
  markers").</p>
  <p>For other reasons, most other fights split the arena between the front and
  back, which leads to the 1 marker being on the NE instead.</p></td></tr>
</table>
</details>

<details markdown=block>
<summary>
  <b>[Damage Down]</b> How strong is the damage down debuff in this fight?
</summary>
<table>
  <tr>
    <td>
      <p>There are actually <em>two</em> different Damage Down debuffs in this 
      encounter, both of which lowers a player's damage by <b>90%</b>.</p>
      <ul>
        <li><em>Damage Down</em> comes from getting hit by avoidable attacks.</li>
        <li><em>Mark of Mortality</em> comes from resolving stacks with less 
        than the required number of players.</li>
      </ul>
      <p>These damage downs also come from two separate debuffs, so <em>they
      stack</em> together for a combined <b>99% damage down!</b></p>
    </td>
    <td style="text-align:center">
      <img src="{{site.baseurl}}/images/ultimates/fru/01/damage_down.png">
      <img src="{{site.baseurl}}/images/ultimates/fru/01/mark_of_mortality.png">
    </td>
  </tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
