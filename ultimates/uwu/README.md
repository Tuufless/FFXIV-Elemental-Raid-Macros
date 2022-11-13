---
layout: default
title: Lv 70. UWU
parent: Ultimates
nav_order: 2
permalink: /ultimates/uwu/
---

# The Weapon's Refrain (Ultimate)

PF largely follows [Clees' UWU guide](http://clees.me/guides/uwu/) with a few differences:

- Ultima is pulled a little **north** after Ultimate Predation instead of south. Eruption baiters will start **south** instead of north.
- Green orbs during Ultimate Annihilation are taken **2211** instead of 3311.

- [**Garuda**](en/01_garuda.md): Midruda
- [**Ifrit**](en/02_ifrit.md): Reverse-Z
- [**Titan**](en/03_titan.md): Mario Kart
- [**Ultimate Predation**](en/04_predation.md)
- [**Ultimate Annihilation**](en/05_annihilation.md): 2211 orbs
- [**Ultimate Suppression**](en/06_suppression.md): Fan Suppression
- [**Primal Roulette**](en/07_primal_roulette.md)

### BiS Notes

- Any gear at or above **i500** will have their substats capped.
- Relic weapons will have their substats capped at **136**.

## Things to note

- There are edge cases to consider if you have a PLD or GNB and skipping Ifrit dashes are a possibility.
	- If you **skip** Ifrit dashes, there is about **6:30** between Ifrit's *first* set of Incinerates and the Homing Lasers after Ultimate Predation (PLD cannot invuln both).
	- If you **don't skip** Ifrit's dashes, there is about **5:40** between Ifrit's *second* set of Incinerates and the Homing Lasers after Ultimate Predation (GNB and PLD cannot invuln both).
- You can fix the tank invuln sequence in Ultima by choosing to tank swap Ifrit's second set of Incinerates instead of using the MT invuln there (although this isn't usually practiced).

## English

```
{% include_relative macros/uwu.en.txt %}
```

## Japanese

```
{% include_relative macros/uwu.jp.txt %}
```

## Markers

- `ABCD`： Orientation.

**Garuda:**
- `4`： Party stack during the two Mistrel Songs ("midruda")

**Ifrit:**
- `ABCD` demarcates the cardinal positions (dodging the first Crimson Charge)

**Titan:**
- `ABCD` and `1`: Titan Gaols.

**Ultima:**
- `3`: Dodging Crimson Charges during Annihilation and the Primal Roulette.
- `4`: Granite Gaol during Suppression.
- `B`: Fireball stack during Suppression.

![](images/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"UWU","MapID":539,"A":{"X":100.0,"Y":0.0,"Z":93.3,"ID":0,"Active":true},"B":{"X":106.7,"Y":0.0,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.0,"Z":106.7,"ID":2,"Active":true},"D":{"X":93.3,"Y":0.0,"Z":100.0,"ID":3,"Active":true},"One":{"X":100.0,"Y":0.0,"Z":100.0,"ID":4,"Active":true},"Two":{"X":107.3,"Y":0.0,"Z":107.3,"ID":5,"Active":true},"Three":{"X":100.0,"Y":0.0,"Z":81.0,"ID":6,"Active":true},"Four":{"X":87.0,"Y":0.0,"Z":87.0,"ID":7,"Active":true}}
```

</details>