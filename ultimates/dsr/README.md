---
layout: default
title: Lv 90. DSR
parent: Ultimates
nav_order: 4
permalink: /ultimates/dsr/
---

# Dragonsong's Reprise (Ultimate)

Elemental's DSR PF strat is still evolving. Use the following macros as a base to start with.

## Summary

For those who are already familiar with the fight, and just need a quick summary:

<table>
  <tr>
    <td><b>Ser Adelphel + Grinnaux</b></td>
    <td><ul><li>HMRT</li></ul></td>
  </tr>
  <tr>
    <td><b>Thordan</b></td>
    <td>
      <ul>
        <li>DRK-relative, role adjust</li>
        <li>Meteors N/S</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>Nidhogg</b></td>
    <td> 
      <ul>
        <li>Easthogg</li>
        <li>4x towers T/M adjust "cw > ccw > across"</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>Eyes</b></td>
    <td>
      <ul>
        <li>DPS blue (or equivalently, T/H red)</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>Alternate Thordan</b></td>
    <td>
      <ul>
        <li>2-2 Anchored Dooms N</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>Double Dragons</b></td>
    <td>
      <ul>
        <li>△ first tethers</li>
        <li>DTTMR Mortal Vow</li>
        <li>Spreads left, stacks right</li>
        <li>1-5 second tethers</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><b>Dragonking Thordan</b></td>
    <td>
      <ul>
        <li>All 3-3-2</li>
      </ul>
    </td>
  </tr>
</table>

### BiS Notes

- Dragonsong's Reprise is the current Ultimate, and is **not** outgeared yet.
    - Use your **i600** BiS.

Looking towards the future:

- Dragonsong's Reprise will not be outgeared until **i730** gear is available.
- Relic weapons (when they arrive) will have their substats capped at **269**.

# Ser Adelphel and Ser Grinnaux

Dragonsong's Reprise is the first Ultimate to showcase a "door" boss. As such, there are two sets of markers and macros to use for this fight.

### Things to check on Party Finder

- Check the marker order for Hyperdimensional Slash (some groups do S→N)

## English
This is the macro that has been going around PF since the beginning:
```
　Adelphel：ST　Grinnaux：MT
【Holy Bladedance】Tether → MT + invuln
【Hyperdimensional Slash】Markers N → S
【Execution】ST invulns
【Silence】ST → D3 → ST
【Playstation chains】
　　D△ T× T□
　　D〇　 　D〇　west: D1>2>3>4: east
　　D□ H× H△
【Haurchefant】
　　　cleave　cleave　　　※ cleaves towards
　　H/R AoE ★ T/M AoE　　　ring (True South)
　　　　　   party
　H1+H2 → D1+D2 → D3+D4 → MT+ST
```

## Markers

All markers are used to bait Hyperdimensional Slashes (black orbs).

![](images/markers_1.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"Adelphel and Grinnaux","MapID":788,"A":{"X":93.015,"Y":0.0,"Z":89.036,"ID":0,"Active":true},"B":{"X":110.964,"Y":0.0,"Z":93.015,"ID":1,"Active":true},"C":{"X":106.985,"Y":0.0,"Z":110.964,"ID":2,"Active":true},"D":{"X":89.036,"Y":0.0,"Z":106.985,"ID":3,"Active":true},"One":{"X":106.985,"Y":0.0,"Z":89.036,"ID":4,"Active":true},"Two":{"X":110.964,"Y":0.0,"Z":106.985,"ID":5,"Active":true},"Three":{"X":93.015,"Y":0.0,"Z":110.964,"ID":6,"Active":true},"Four":{"X":89.036,"Y":0.0,"Z":93.015,"ID":7,"Active":true}}
```

</details>

# King Thordan
### Things to check on Party Finder

- Check the Meteor tower positions + outside tower priority.
- Check how the group resolves Nidhogg towers.

## English
```
―《Thordan》――――――――――――――――――
【Strength of the Ward】
　　North (West)　　South (East)
　　　　   H1　　　　　　  H2
　　　D1 MT D3　　　D2 ST D4
　■ Skyward Leaps + Towers
　　※ Use Thordan as north
　　Cross tethers：
　　　MT：West tether → East of party
　　　ST：East tether → West of party
【Sanctity of the Ward】
　■ Sacred Severs (Zephirin-relative)
　　Group 1 (MTH1D1D3) → Opposite Zephirin
　　Group 2 (STH2D2D4) → Beside Zephirin
　　※ Swap between roles to resolve swords
　■ Meteors
　　　　　MT/D3　　　 ※ Fix Meteors N/S
　　　H1/D1　H2/D2　※ Meteors run cw
 　　　　　ST/D4
　　※ Meteor group (T/H or DPS) outside
　　　　　　　　center > ccw > cw
　　※ Meteor grp → Final cardinal towers
　　※ Non-meteor grp → Clockwise from ice
―《Nidhogg》("Easthogg") ―――――――――――
【Dive from Grace】
　　　　　　　　　   ②↑  ②↓
　　　  ②③　　　　　   ①　　　　　   ①③
　　①↑▲ ①↓  →  ③↑▲ ③↓  →  ②↑▲ ②↓
　　　　①　　　　　　 ③　　　　　　 ①
　　※ Face east when placing towers
【4x Towers (H/R fixed)】
　　MT/D3　ST/D4　　Tanks/Melee adjust：
　　　　　  ●　　　　　　cw > ccw > across
　　H1/D1　H2/D2
　※ H/R bait Geirskogul
　■ Soul Tethers
　　MT → Nidhogg's tether (under boss)
　　ST → clone's tether
―《Eyes phase》――――――――――――――――
　　　D1　　D4　　T/H → Red tethers
　　　MT　　ST　　DPS → Blue tethers
　　　H1　　H2　　※ Stack on Estinien in mid
　　　D2　　D3　　　　to swap tethers
　【Yellow+Blue Orbs】
　　　　D1　　D4　　　　※ DPS goes to T/H
　MTH1　　　　　STH2　　　to swap tethers
　　　　D2　　D3
　【Mirage Dives】
　■ Initial spread　■ Swaps (from true North)
　　　D1　　D4　 　 1. ccw：H1>H2：cw
　　　　  T+H　　　　2. ccw：MT>ST：cw
　　　D2　　D3　  　3. ccw：D1>D2>D3>D4：cw
　※ Around blue eye
―《Alternate Timeline Thordan》―――――――
【Wrath of the Heavens】
　North：MT>ST>H1>H2>D1>D2>D3>D4：South
　　　　　▼　★　▼
　　(blue)　\　  /　　　　　※ Use white dragon
　　　　　　　\/　　(party)　　　as North
　　　　　　  /　\　
　　　(tether)　(tether)
【Death of the Heavens】(2-2 Dooms north)
　■ Initial spread
　　　　　　　　　※ Use Grinnaux as North
　　　　　　　　　　　　 = Dooms
　　①　　　　④　　　　(dodge 2nd Impact)
　　　　　　　　　　　　① = Non-doom
　　　　②　　③　　　　　　(dodge 3rd Impact)
　■ Playstation 2 (Anchored Dooms)
　　(△/□) × (△/□)　  ※  +  bait circles
　　　 　　　　　　※ Doom players stay
　　　　 × 　　　　　non-doomed adjust
　■ Meteors：Caster LB2 (centered at N)
―《Double Dragons》 (△, DTTMR, 1-5) ―――――
　(North)　MT H1 D1 D3 → Nidhogg　
　(South)　ST H2 D2 D4 → Hraesvelgr
【Dread/Great Wyrmsbreath #1】
　MT　　　　ST　　
　　　　　　　　　　※ H1, H2, D4 stays
　　　D3D4　　　　※ D1, D2, D3 adjusts
　H1D1　　H2D2
【Hallowed Wings】MT → N/W　　ST → S/E
【Mortal Vow】(pass in mid except last) 
　　DPS → MT → ST → D1/D2 → D3
【Wroth Flames】Purple → Left　White → Right
【Dread/Great Wyrmsbreath #2】(1-5)
　H1 north, everyone else south
【Cauterize】(2x invuln) MT → West, ST → east
―《Dragonking Thordan》―――――――――――
【Mitigations】
　All with H2 30s, shields and:
　　Alt. End：MT 90s, ST 90s, H2 120s, D3
　　AM1：MT Rep, H1 120s, H2 120s, D1
　　Giga1： ST Rep, D2, D4
　　AM2：MT Rep, MT 90s, ST 90s, H1 180s
　　Giga 2：ST Rep, D1, D3
　　AM3：MT Rep, H1 120s, H2 120s, D2, D4
【Trinity】After Exaflare → D1, D2
　　　　　 After Akh Morn → D3, D4
　　　　　 After Gigaflare → H1, H2
【Akh Morn's Edge】(All 3-3-2)
　　H1D1D3　　H2D2D4
　　　　　　 MTST
```

## Markers

I personally really like "inside" markers.

![](images/markers_2.jpg)
<details markdown=block>
<summary>XIVLauncher WaymarkPresetPlugin positions</summary>

```json
{"Name":"Dragonsong's Reprise","MapID":788,"A":{"X":100.0,"Y":0.0,"Z":87.0,"ID":0,"Active":true},"B":{"X":113.0,"Y":0.0,"Z":100.0,"ID":1,"Active":true},"C":{"X":100.0,"Y":0.0,"Z":113.0,"ID":2,"Active":true},"D":{"X":87.0,"Y":0.0,"Z":100.0,"ID":3,"Active":true},"One":{"X":109.192,"Y":0.0,"Z":90.808,"ID":4,"Active":true},"Two":{"X":109.192,"Y":0.0,"Z":109.192,"ID":5,"Active":true},"Three":{"X":90.808,"Y":0.0,"Z":109.192,"ID":6,"Active":true},"Four":{"X":90.808,"Y":0.0,"Z":90.808,"ID":7,"Active":true}}
```

</details>
