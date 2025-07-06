---
layout: default
title: Lv 100. FRU (v1.0)
nav_order: 6
has_children: true
has_toc: false
permalink: /static/fru/
---

# Futures Rewritten (Ultimate) v1.0

This documentation is primarily for my static, and is **not** what PF does (in 
both Elemental and Mana).

You are welcome to take the ideas here for your own static if you so wish.

That being said, having cleared FRU with this strat (and also having cleared 
FRU a number of times with Mana PF strats, [there *are* some things I would 
tweak](#things-i-would-change-for-v20), if you would like to consider them.)

![]({{site.baseurl}}/images/ultimates/fru/clear_ss.jpg)

### BiS Notes

- Use your **i730** BiS.
- Use the highest grade potions available.

Looking towards the future:

- Futures Rewritten will not be outgeared until **i860** gear is available in
Patch 8.0.
- Relic weapons (when they arrive) will have their substats capped at **393**.

<div>
  <a href="{{site.baseurl}}/fru_cheatsheet.jpg">
    <img src="{{site.baseurl}}/fru_cheatsheet.jpg">
  </a>
</div>

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

---

## Things I would change for v2.0

As mentioned above, although my first static used the strategies documented 
here for our clear, there *are* things I would change if I were to do it again.

**Markers:** I would consider testing out markers in a square formation:

![]({{site.baseurl}}/images/ultimates/fru/square_markers.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{
  "Name":"FRU (Square markers)",
  "MapID":1006,
  "A":{"X":100.0,"Y":0.0,"Z":93.0,"ID":0,"Active":true},
  "B":{"X":107.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},
  "C":{"X":100.0,"Y":0.0,"Z":107.0,"ID":2,"Active":true},
  "D":{"X":93.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},
  "One":{"X":93.0,"Y":0.0,"Z":93.0,"ID":4,"Active":true},
  "Two":{"X":107.0,"Y":0.0,"Z":93.0,"ID":5,"Active":true},
  "Three":{"X":107.0,"Y":0.0,"Z":107.0,"ID":6,"Active":true},
  "Four":{"X":93.0,"Y":0.0,"Z":107.0,"ID":7,"Active":true}
}
```

</details>
- In particular, the cardinal `ABCD` markers are closer towards the center, and
line up with the boss's targeting circle in P5, making them the center point
for all Exaline dodges during *Fulgent Blade*.
- However, I'm not sure if the intercardinal markers are *too* close for the 
vertical *Burnt Strikes* in P1 (although this is minor), and whether 
*Apocalypse* gets confusing with the markers in a square formation.

**P1:** I would tweak some parts to follow Mana (although keep the ST's base 
position East):
- *Cyclonic Break*: I would *not* do coloured sectors, but instead have 
everybody rotate clockwise for Lightning spreads instead. This keeps the 
healers closer to the center.
- *Fall of Faith*: I would line up West-to-East (and resolve the tethers West 
and East), instead of lining up North-to-South. This is more minor, since the 
North-to-South lineup is just for convenience since the tethers at the end of 
*Utopian Sky* are North and South, but lining up horizontally makes it slightly 
easier to discern the second, third, and fourth tethers as they all originate 
perpendicular to the lineup.
- *Towers*: This is a minor tweak, but I would do a hybrid- I would have the
base positions as D1/H1 north, D2/H2 mid, D3/D4 south (which resembles Mana), 
but I would *keep* how the party adjusts for towers (don't count from the North 
like Mana).

**P2:** I would change some parts to follow Mana (not updating *Mirror, 
Mirror*).
- *Diamond Dust*: I would *not* do coloured sectors, but have the whole party 
rotate clockwise if needed instead. This keeps the movement consistent across 
the whole party (instead of having T/H go anti-clockwise, DPS clockwise).
- *Light Rampant*: I would *not* drop the puddles starting E/W and going 
anti-clockwise. This is a minor point, but the "L-shaped" style that is very
common elsewhere is also compatible with the way Mana drops puddles, so I feel
leaving this up to the individual to choose which they prefer is better.

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
