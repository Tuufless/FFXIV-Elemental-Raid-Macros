---
layout: default
title: Lv 90. DSR
nav_order: 4
has_children: true
has_toc: false
permalink: /elemental/dsr/
---

# Dragonsong's Reprise (Ultimate)

Elemental's DSR PF strat can be broken down as follows:

- [**The Holy See**](01_the_holy_see): HMRT
- [**King Thordan**](02_thordan): DRK-relative, role adjust
- [**Nidhogg**](03_nidhogg): Easthogg
- [**Eyes**](04_eyes): T/H red, DPS blue
- [**Alternate Timeline Thordan**](05_alternate_thordan):
  2-2 Dooms North, Anchored Dooms
- [**Double Dragons**](06_double_dragons): △ WB1, DTTMR
  Mortal Vow, 5-1 WB2
- [**Dragonking Thordan**](07_dragonking_thordan): All 3-3-2

### BiS Notes

- Any gear at or above **i730** will have their substats capped.
- Relic weapons will have their substats capped at **269**.
- Use the highest available food and potions.

<a href="{{site.baseurl}}/dsr_cheatsheet.jpg">
  <img src="{{site.baseurl}}/dsr_cheatsheet.jpg">
</a>
*(Other languages: [日本語]({{site.baseurl}}/dsr_cheatsheet_jp.jpg))*

---

## PoVs

Here are some clear PoVs that I've been collecting.

- [MT PoV (WAR)](https://youtube.com/live/yRJrvYChhWQ)
- [ST PoV (PLD)](https://youtube.com/live/7iFsy8xbeSc)
- [H1 PoV (WHM)](https://youtube.com/live/UJEpzF2nJo8)
- [H2 PoV (SCH)](https://youtube.com/live/qwVJPkc5un0)
- [D1 PoV (SAM)](https://youtube.com/live/2TOyLsYQlJo)
- [D2 PoV (NIN)](https://youtube.com/live/XOgCkE9Jdts)
- [D3 PoV (DNC)](https://youtube.com/live/mGSpsIZXRpc)
- [D4 PoV (BLM)](https://youtube.com/live/zVVuQysS9po)

---

## Things to note

- Using automarkers to mark Thunder players in Wroth of the Heavens, and
  especially Wroth Flames is considered the norm (*use at your own risk*).

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

![]({{site.baseurl}}/images/ultimates/dsr/markers_1.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"DSR P1 - The Holy See",
  "MapID":788,
  "A":{"X":95.0,"Y":0.0,"Z":91.5,"ID":1,"Active":true},
  "B":{"X":108.5,"Y":0.0,"Z":95.0,"ID":2,"Active":true},
  "C":{"X":105.0,"Y":0.0,"Z":108.5,"ID":5,"Active":true},
  "D":{"X":91.5,"Y":0.0,"Z":105.0,"ID":6,"Active":true},
  "One":{"X":105.0,"Y":0.0,"Z":91.5,"ID":3,"Active":true},
  "Two":{"X":108.5,"Y":0.0,"Z":105.0,"ID":4,"Active":true},
  "Three":{"X":95.0,"Y":0.0,"Z":108.5,"ID":7,"Active":true},
  "Four":{"X":91.5,"Y":0.0,"Z":95.0,"ID":0,"Active":true}
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

PF uses the "inner" markers. All markers demarcate:

- The boundaries for the charges at the start of Strength of the Ward.
- The boundary for Nidhogg's Drachenlance.

In addition, the intercardinal square markers indicate:

- Where to stand to bait the towers in Nidhogg.
- The boundary of Hot Tail in the Double Dragons phase.

![]({{site.baseurl}}/images/ultimates/dsr/markers_2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"Dragonsong's Reprise",
  "MapID":788,
  "A":{"X":100.0,"Y":0.0,"Z":87.0,"ID":0,"Active":true},
  "B":{"X":113.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":113.0,"ID":2,"Active":true},
  "D":{"X":87.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":109.192,"Y":0.0,"Z":90.807,"ID":4,"Active":true},
  "Two":{"X":109.192,"Y":0.0,"Z":109.192,"ID":5,"Active":true},
  "Three":{"X":90.807,"Y":0.0,"Z":109.192,"ID":6,"Active":true},
  "Four":{"X":90.807,"Y":0.0,"Z":90.807,"ID":7,"Active":true}
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