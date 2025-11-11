---
layout: default
title: Lv 90. DSR (Mana)
nav_order: 4
has_children: true
has_toc: false
permalink: /mana/dsr/
---

# Dragonsong's Reprise (Ultimate)

Mana PF follows [Lily Doll's DSR strat](https://na.finalfantasyxiv.com/lodestone/character/34120564/blog/5178834/):

- [**The Holy See**](01_the_holy_see): HMRT
- [**King Thordan**](02_thordan): DRK-relative, role adjust
- [**Nidhogg**](03_nidhogg): Westhogg
- [**Eyes**](04_eyes): T/H blue, DPS red
- [**Alternate Timeline Thordan**](05_alternate_thordan):
  2-2 Dooms South, Anchored Dooms
- [**Double Dragons**](06_double_dragons): △ WB1, DTTMR
  Mortal Vow, fixed WB2
- [**Dragonking Thordan**](07_dragonking_thordan): All 3-3-2

### BiS Notes

- Any gear at or above **i730** will have their substats capped.
- Relic weapons will have their substats capped at **269**.
- Use the highest available food and potions.

---

# The Holy See

Dragonsong's Reprise is the first Ultimate to showcase a "door" boss. As such,
there are two sets of markers and macros to use for this fight.

## English

{% include_relative macros/dsr_1.en.md %}

<details markdown=block>
<summary>日本語</summary>

{% include_relative macros/dsr_1.jp.md %}

</details>

## Markers

All markers are used to bait Hyperdimensional Slashes (black orbs).

![]({{site.baseurl}}/images/ultimates/dsr_mana/markers_1.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"DSR P1 (Mana)",
  "MapID":788,
  "A":{"X":90.0,"Y":0.0,"Z":95.0,"ID":0,"Active":true},
  "B":{"X":95.0,"Y":0.0,"Z":90.0,"ID":1,"Active":true},
  "C":{"X":105.0,"Y":0.0,"Z":90.0,"ID":2,"Active":true},
  "D":{"X":110.0,"Y":0.0,"Z":95.0,"ID":3,"Active":true},
  "One":{"X":90.0,"Y":0.0,"Z":105.0,"ID":4,"Active":true},
  "Two":{"X":95.0,"Y":0.0,"Z":110.0,"ID":5,"Active":true},
  "Three":{"X":105.0,"Y":0.0,"Z":110.0,"ID":6,"Active":true},
  "Four":{"X":110.0,"Y":0.0,"Z":105.0,"ID":7,"Active":true}
}
```

</details>

---

# King Thordan

This is the macro for the bulk of the fight.

## English

{% include_relative macros/dsr_2.en.md %}

<details markdown=block>
<summary>日本語</summary>

{% include_relative macros/dsr_2.jp.md %}

</details>

## Markers

Mana PF uses the "outer" markers.

![]({{site.baseurl}}/images/ultimates/dsr_mana/markers_2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"DSR P2 (Mana)",
  "MapID":788,
  "A":{"X":100.0,"Y":0.0,"Z":80.767,"ID":0,"Active":true},
  "B":{"X":119.232,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":119.232,"ID":2,"Active":true},
  "D":{"X":80.767,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":113.599,"Y":0.0,"Z":86.401,"ID":4,"Active":true},
  "Two":{"X":113.599,"Y":0.0,"Z":113.599,"ID":5,"Active":true},
  "Three":{"X":86.401,"Y":0.0,"Z":113.599,"ID":6,"Active":true},
  "Four":{"X":86.401,"Y":0.0,"Z":86.401,"ID":7,"Active":true}
}
```

</details>

---

## Frequently Asked Questions

<details markdown=block>
<summary><b>[Damage Down]</b> How strong is the damage down debuff in this
fight?</summary>
<table>
  <tr><td><p>The Damage Down debuff in this phase lowers a player's damage by
  <b>50%</b>.</p></td></tr>
</table>
</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>