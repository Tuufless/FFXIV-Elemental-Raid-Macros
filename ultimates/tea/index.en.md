---
layout: default
title: Lv 80. TEA
parent: Ultimates
nav_order: 3
has_children: true
has_toc: false
permalink: /ultimates/tea/
---

# The Epic of Alexander (Ultimate)

Since Elemental PF hasn't agreed on a TEA strat since Patch 5.1, I'm going to take the liberty of piecing one together myself. This is what I would do:

- [**Living Liquid**](01_living_liquid.en.md): Modified Separations (the "JP strat")
- [**Limit Cut**](02a_limit_cut.en.md): 1211 or 1256
- [**Brute Justice + Cruise Chaser**](02b_bjcc.en.md): Tollgate (this is my strat that I use)
- [**Alexander Prime**](03_alex_prime.en.md): 09STOP Wormhole (Korean sim strat- this is also called "Onyxia" by NA/EU)
- [**Perfect Alexander**](04_perfect_alex.en.md)

### Things to check

- The Esuna priority for Living Liquid's Throttles (Esuna self first or not)
- The Limit Cut strategy (1211 vs. 1256)

### BiS Notes

- Any gear at or above **i595** will have their substats capped.
- Relic weapons will have their substats capped at **184**.
- The lowest potions you can use and still get maximum benefits are **HQ Grade 6 Tinctures**.

![]({{site.baseurl}}/images/ultimates/tea/tea_cheatsheet.jpg)
*(Full-size image: [English]({{site.baseurl}}/images/ultimates/tea/tea_cheatsheet.jpg), [日本語]({{site.baseurl}}/images/ultimates/tea/tea_cheatsheet_jp.jpg))*

---

## PoVs

Here are some clear PoVs that I've been collecting.

- [MT PoV (WAR)](https://youtu.be/uJVHsrhHsJ8)
- [ST PoV (PLD)](https://youtu.be/leQ9t61W4OY)
- [H1 PoV (WHM)](https://youtu.be/IqcxKunPY5Q)
- [H2 PoV (SGE)](https://youtu.be/Q80yoHMcxhg)
- [D1 PoV (SAM)](https://youtu.be/RCkbxPT3prI)
- [D2 PoV (NIN)](https://youtu.be/yb9oLIlwiCM)
- [D3 PoV (DNC)](https://youtu.be/ToaYJdOdUcA)
- [D4 PoV (RDM)](https://youtu.be/coE2xYyd23A)

---

## English

```
{% include macros/ultimates/tea.en.txt %}
```

<details markdown=block>
<summary>日本語</summary>

```
{% include macros/ultimates/tea.jp.txt %}
```

</details>

---

## Markers

- `ABCD` are for orientation

**Limit Cut:**
- `1234` divides the arena for Limit Cut
	- If doing 1211, start from the first explosion on the non-marked side.
	- If doing 1256, the 1256 group goes to the side without markers. The 3478 group goes to the side with markers.
	
**Brute Justice + Cruise Chaser:**
- `A`: 1st Water
- `C`: 2nd Water
- `3`: 3rd Water

**Alexander Prime:**
- `4`: Party stack for Inception Formation (except for ST, healers, and blue-tether DPS)

**Perfect Alexander:**
- `B`: Dark Beacon (Forced March, Fate Calibration Beta)
- `1234`: Exatrine

![]({{site.baseurl}}/images/ultimates/tea/markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"TEA",
  "MapID":694,
  "A":{"X":100.0,"Y":0.0,"Z":88.0,"ID":0,"Active":true},
  "B":{"X":114.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":116.0,"ID":2,"Active":true},
  "D":{"X":84.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":92.2,"Y":0.0,"Z":107.8,"ID":4,"Active":true},
  "Two":{"X":100.0,"Y":0.0,"Z":107.8,"ID":5,"Active":true},
  "Three":{"X":107.8,"Y":0.0,"Z":107.8,"ID":6,"Active":true},
  "Four":{"X":107.8,"Y":0.0,"Z":100.0,"ID":7,"Active":true}
}
```

</details>

<script data-goatcounter="https://tuufless.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>