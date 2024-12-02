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

<div style="background-color: #200 ; padding: 10px; border: 1px solid;">
<ul>
  <li><b>In the interest of getting a working strat documented, I have decided
  to document Lucrezia's strat.</b>
    <ul>
      <li>Lucrezia actually has multiple groups- although Lucrezia has 
      released video guides and Idyllshire has a written guide, I will instead 
      start by referencing what their <em>streaming team</em> does, as the 
      video and written guides do not have sufficient detail, and I need to 
      check how mechanics are resolved over multiple pulls.</li>
      <li>As a result, this <em>may</em> have some differences from the 
      "Lucrezia" strat done on Mana.</li>
    </ul>
  </li>
  <li><b>For now, the focus is on getting something written down
  <em>without</em> having to debate the merits of each strategy.</b></li>
  <li><b>Once more groups have cleared and we have more information, some 
  things will likely be modified- again, the focus is to get <em>something</em>
  workable first.</b></li>
  <li><b>This will be a time-intensive process- a final strategy likely won't 
  come until the end of Patch 7.1 (roughly March/April 2025).</b></li>
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
        <li>One comes from getting hit by avoidable attacks.</li>
        <li>One comes from resolving stacks with fewer people.</li>
      </ul>
      <p>Because these damage downs come from two separate debuffs, <em>they
      stack</em> together for a combined <b>99% damage down!</b></p>
    </td>
  </tr>
</table>
</details>
