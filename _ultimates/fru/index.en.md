---
layout: default
title: Lv 100. FRU (WIP)
nav_order: 6
has_children: true
has_toc: false
permalink: /ultimates/fru/
---

# Futures Rewritten (Ultimate)

Elemental's FRU PF strat is currently a **work in progress**.

<div style="padding: 10px; border: 1px solid;">
<ul>
  <li><b>Current version: v2.0.0</b>
    <ul>
      <li>Fatebreaker: v2.0.0</li>
      <li>Usurper of Frost: v2.0.0</li>
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
  and likely won't settle until the end of Patch 7.1 (roughly March/April 2025).</b></li>
</ul>
</div>

### BiS Notes

- Use your **i730** BiS.
- Relic weapons (when they arrive) will have their substats capped at **393**.
- Use the highest grade potions available.

## Markers

![]({{site.baseurl}}/images/ultimates/fru/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"FRU",
  "MapID":1006,
  "A":{"X":100.0,"Y":0.0,"Z":87.0,"ID":0,"Active":true},
  "B":{"X":113.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":113.0,"ID":2,"Active":true},
  "D":{"X":87.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":90.808,"Y":0.0,"Z":90.808,"ID":4,"Active":true},
  "Two":{"X":109.192,"Y":0.0,"Z":90.808,"ID":5,"Active":true},
  "Three":{"X":109.192,"Y":0.0,"Z":109.192,"ID":6,"Active":true},
  "Four":{"X":90.808,"Y":0.0,"Z":109.192,"ID":7,"Active":true}
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
  <p>For other reasons, most other fights split the arena between the front and back, which leads to the 1 marker being on the NE instead.</p></td></tr>
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
        than four players.</li>
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
